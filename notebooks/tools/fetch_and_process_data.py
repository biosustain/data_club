import os
import pandas as pd

BASE_URL = "https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-022-30513-2/MediaObjects/" 
PROTEOME_URL = os.path.join(BASE_URL, "41467_2022_30513_MOESM4_ESM.xlsx")
TRANSCRIPTOME_URL = os.path.join(BASE_URL, "41467_2022_30513_MOESM6_ESM.xlsx")

raw_proteome_data, raw_transcriptome_data = (
    pd.read_excel(url, header=0) for url in (PROTEOME_URL, TRANSCRIPTOME_URL)
)

proteome_data = (
    raw_proteome_data
    .drop(columns=["Unnamed: 0", "Categories"])  # remove unwanted columns
    .dropna(how="any")                           # remove rows with any null values
)
transcriptome_data = (
    raw_transcriptome_data
    .dropna(how="any")                           # remove rows with any null values
)

# Get columns with numeric dtypes
numeric_transcriptome_columns, numeric_proteome_columns = (
    [
        c for c, dtype in df.dtypes.items() 
        if pd.api.types.is_numeric_dtype(dtype)
    ]
    for df in [transcriptome_data, proteome_data]
)

print("Proteome data:")
print(proteome_data.head())
proteome_data.to_csv("proteome_data.csv", index=False)

print("Transcriptome data:")
print(transcriptome_data.head())
transcriptome_data.to_csv("transcriptome_data.csv", index=False)


