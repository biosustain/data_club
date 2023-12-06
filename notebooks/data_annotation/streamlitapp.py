import os

import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from matplotlib.dates import DateFormatter

from uniprot_api import get_protein_info, extract_protein_info

# Reading data in
data_dir = "../../data"

transcriptome_df = pd.read_csv(os.path.join(data_dir, "transcriptomics.tsv"), sep='\t', index_col=False)
proteome_df = pd.read_csv(os.path.join(data_dir,"proteomics.tsv"), sep='\t', index_col=False)

times = [float(s.split(" ")[0]) for s in transcriptome_df.columns if s != "mRNA"]
transcriptome_df.columns = ["mRNA"] + times
proteome_df.columns = ["Majority protein IDs"] + times

intersection = list(set(transcriptome_df["mRNA"].unique()).intersection(proteome_df["Majority protein IDs"].unique()))
#st.write("Intersection before annotation", intersection)

transcriptome_df = pd.read_csv(os.path.join(data_dir, "transcriptomics_mapped.tsv"), sep='\t', index_col=False)
intersection = list(set(transcriptome_df["Accessions"].unique()).intersection(proteome_df["Majority protein IDs"].unique()))
#st.write("Intersection after annotation", intersection)

transcriptome_df = transcriptome_df[transcriptome_df["Accessions"].isin(intersection)]
iter_csv = pd.read_csv(os.path.join(data_dir,'sgd_goa.tsv'), sep='\t', iterator=True, chunksize=1000)
go_df = pd.concat([chunk[chunk['ids'].isin(transcriptome_df["mRNA"].unique())] for chunk in iter_csv])
go_df = transcriptome_df[["mRNA", "Accessions"]].set_index("mRNA").join(go_df.set_index("ids")).drop_duplicates()

transcriptome_df = transcriptome_df.drop("mRNA", axis=1)
transcriptome_df.columns = times + ["Accessions"]
proteome_df = proteome_df[proteome_df["Majority protein IDs"].isin(intersection)]




# Dashboard
st.title("Saccharomyces Cerevisiae app")

# Use st.selectbox to let the user choose an option
mrna = st.selectbox("Choose an mRNA/protein:", transcriptome_df["Accessions"].unique())
response = get_protein_info(accession=mrna)
info = extract_protein_info(accession=mrna, response=response)
st.write(info)

# st.write also works for showing dataframes, and can have many args
mrna_df = transcriptome_df.set_index("Accessions").loc[[mrna]]
st.write(f"mRNA levels for {mrna}:", mrna_df)
print(mrna_df.shape)
prot_df = proteome_df.set_index("Majority protein IDs").loc[[mrna]]
st.write(f"Protein intensity for {mrna}:", prot_df)
print(prot_df.shape)

print(prot_df.loc[[mrna]].values)

# streamlit can display matplotlib plots that change depending on the selectbox
f, ax = plt.subplots()
for _, row in mrna_df.iterrows():
    ax.plot(times, row.values, marker="x", linestyle="dotted", linewidth=1)
    ax.plot(times, prot_df.loc[[mrna]].T.values, marker="o", linestyle="dotted", linewidth=1)
    ax.set(title=f"Timecourse for mRNA {mrna}", xlabel="Time", ylabel="Measurement")
    ax.xaxis.set_major_formatter(DateFormatter("%H:%m"))
st.write("Here is a matplotlib plot of this data:")
st.pyplot(f)

# How to use altair for plots with tooltips
st.write(
    """
    Next we use altair to plot a bunch of mRNAs whose names share the same
    starting characters, with the name of the mRNA for each timecourse shown in
    a tooltip.
    """
)

transcriptome_df = transcriptome_df.set_index("Accessions").join(go_df.set_index("Accessions")).reset_index()
proteome_df = proteome_df.set_index("Majority protein IDs").join(go_df.set_index("Accessions")).reset_index()

go = st.selectbox("Choose a GO term:", go_df["go"].unique())
go_tr_df = (
    transcriptome_df.set_index("go").loc[[go]]
    .melt(id_vars=["Accessions"], var_name="time", value_name="mRNA measurement")
)
go_tr_df["type"] = "transcriptome"

go_pr_df = (
    proteome_df.set_index("go").loc[[go]]
    .melt(id_vars=["Majority protein IDs"], var_name="time", value_name="protein measurement")
)
go_pr_df["type"] = "proteome"

chart = (
    alt.Chart(go_tr_df)
    # next line tells altair to make a line plot with circles at the points
    .mark_line(point=alt.OverlayMarkDef(filled=False, fill="white"))
    # indicate which columns are for axes and which for colour and tooltip text
    .encode(x="time", y="mRNA measurement", color=alt.Color("Accessions", legend=None))
)
st.altair_chart(chart, use_container_width=True)


chart = (
    alt.Chart(go_pr_df)
    # next line tells altair to make a line plot with circles at the points
    .mark_line(point=alt.OverlayMarkDef(filled=False, fill="white"))
    # indicate which columns are for axes and which for colour and tooltip text
    .encode(x="time", y="protein measurement", color=alt.Color("Majority protein IDs", legend=None))
)
st.altair_chart(chart, use_container_width=True)
