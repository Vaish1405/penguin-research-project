from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

project = Path("Penguin Research Project")
data_folder = project / "data"
output_folder = project / "outputs"

# read the input file
input_csv = output_folder / "penguins_size_clean.csv"

# convert to a dataframe
penguins_df = pd.read_csv(input_csv)

species_df = penguins_df["species"].value_counts()

# plt.figure
# species_df.plot(kind="bar")
# plt.title("Count for each penguin species: ")
# plt.xlabel("species: ")
# plt.ylabel("# of penguins")
# plt.xticks(rotation=40)
# plt.tight_layout()
# plt.savefig(output_folder / "bar_species_count.png", dpi=300)
# plt.show()

# print(type(species_df))


# to get the bodymass for each species categories
# species_body_mass = penguins_df.groupby("species")["body_mass_g"].mean()
# species_body_mass.plot(king="hist") # <-- this is the default pandas way of doing
# plt.savefig(output_folder / "hist_species_body_mass_pandas.png", dpi=300)

# species_body_mass.plot(kind="hist")
# plt.hist(penguins_df["body_mass_g"], bins=5, color="pink", edgecolor="black")
# plt.title("Showing different species for range of body mass")
# plt.xlabel("Body mass")
# plt.ylabel("# of penguin species")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.savefig(output_folder / "hist_species_body_mass.png", dpi=300)

# add a scatter plot for flipper length vs body mass
# plt.scatter(penguins_df["flipper_length_mm"], penguins_df["body_mass_g"])
# plt.title("Flipper length vs. Body mass")
# plt.xlabel("Flipper Length")
# plt.ylabel("Body Mass")
# plt.xticks(rotation=0)
# plt.grid(True, alpha=0.2)
# plt.tight_layout()
# plt.savefig(output_folder / "scatter_flipper_mass.png", dpi=300)

# box plot -- also share the pandas version
# penguins_df.boxplot(column="body_mass_g", by="species")
# plt.title("Box plot for body mass organized by species")
# plt.xlabel("Species")
# plt.ylabel("Body Mass")
# plt.xticks(rotation=0)
# plt.grid(True, alpha=0.2)
# plt.tight_layout()
# plt.savefig(output_folder / "box_species_body_mass", dpi=300)

# multi label graphs
# x - species
# y - both the length, depth of the culmen
# have a dataframe for species, culmen length 

# cul_df.plot(kind="bar")
# plt.show()
stu = ["a", "b", "c", "d"]
x = [1, 2, 3, 4]
y = [4, 6, 8, 10]

plt.figure()
plt.bar(stu, x, label="First Exam Scores", color="red")
plt.bar(stu, y, label="Second Exam")
plt.xlabel("Students")
plt.ylabel("Scores for both exams")
plt.legend()
plt.show()