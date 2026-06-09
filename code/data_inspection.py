from pathlib import Path
import pandas as pd

project = Path("Penguin Research Project")
data_folder = project / "data"
output_folder = project / "outputs"

# read the input file
input_csv = data_folder / "penguins_size.csv"

# convert to a dataframe
penguins_df = pd.read_csv(input_csv)

# Basic facts
df_shape = penguins_df.shape
row_count = penguins_df.shape[0] # row_count 
column_count = penguins_df.shape[1] # column_count
column_names = penguins_df.columns # column names
missing_values = penguins_df.isna().sum() # missing_columns with the number of missing values

# category count for a specific column
if "species" in penguins_df.columns:
    species_count = penguins_df["species"].value_counts()

# Descriptive values
head_val = penguins_df.head() # first 5 values
tail_val = penguins_df.tail() # last 5 values
d_types_df = penguins_df.dtypes # type of data for each column
df_desc = penguins_df.describe() # numeric values -- mean, std, max, quartiles, (median)

# Get values for specific columns
sex_val = penguins_df["sex"]

# rename the columns to body length and depth
names = {
    "culmen_length_mm": "body_length",
    "culmen_depth_mm": "body_depth"
}
penguins_df = penguins_df.rename(columns=names)

# drop all na values from the dataframe
penguins_df_clean = penguins_df.dropna()

# clean df to a csv file
output_file_path = output_folder / "clean_csv_output.csv"
penguins_df_clean.to_csv(output_file_path, index=False)

review_output = output_folder / "inspection.txt"
with open(review_output, 'a') as file:
    file.write(f"Shape of the dataframe: {df_shape}\n")
    file.write(f"# of rows: {row_count}\n")
    file.write(f"# of columns: {column_count}\n")

    file.write(f"Column names:\n")
    for column in column_names:
        file.write(f"- {column}\n")

    file.write(f"Species count for each category: {species_count}\n")
    file.write(f"Top 5 rows: {head_val}\n")
    file.write(f"Bottom 5 rows: {tail_val}\n")
    file.write(f"Datatypes of each column: {d_types_df}\n")
    file.write(f"Numeric values for all data: {df_desc}\n")
    
