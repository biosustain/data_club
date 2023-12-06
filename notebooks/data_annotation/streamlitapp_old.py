import os

import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from matplotlib.dates import DateFormatter

data_dir = "../../data"

transcriptome_df = pd.read_csv(os.path.join(data_dir, "transcriptomics.tsv"), sep='\t', index_col=False)
proteome_df = pd.read_csv(os.path.join(data_dir,"proteomics.tsv"), sep='\t', index_col=False)
times = [float(s[:-4]) * 3600 for s in transcriptome_df.columns if s != "mRNA"]
transcriptome_df.columns = ["mRNA"] + times

st.title("An example streamlit app")

# The function for printing things is st.write
st.write("This page visualises our example transcriptomics data.")

# Use st.selectbox to let the user choose an option
mrna = st.selectbox("Choose an mRNA:", transcriptome_df["mRNA"].unique(), index=1590)

# st.write also works for showing dataframes, and can have many args
mrna_df = transcriptome_df.set_index("mRNA").loc[[mrna]]
st.write(f"Here is the data for mRNA {mrna}:", mrna_df)

# streamlit can display matplotlib plots that change depending on the selectbox
f, ax = plt.subplots()
for _, row in mrna_df.iterrows():
    ax.plot(times, row.values, marker="x", linestyle="dotted", linewidth=1)
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
# Series.str.extract is handy for doing regexes on string columns
prefixes = transcriptome_df["mRNA"].str.extract(r"([^\d]*)")[0]
prefix = st.selectbox(
    "Choose a prefix i.e. the start of the mRNA's name up to the first digit:",
    prefixes.unique(),
)
prefix_df = (
    transcriptome_df
    # loc works here because prefixes has the same index as transcriptome_df
    .loc[prefixes == prefix]
    # melt is more succinct than stack + rename here
    .melt(id_vars=["mRNA"], var_name="time", value_name="measurement")
)
chart = (
    alt.Chart(prefix_df)
    # next line tells altair to make a line plot with circles at the points
    .mark_line(point=alt.OverlayMarkDef(filled=False, fill="white"))
    # indicate which columns are for axes and which for colour and tooltip text
    .encode(x="time", y="measurement", color=alt.Color("mRNA", legend=None))
)
st.altair_chart(chart, use_container_width=True)
