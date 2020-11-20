# %% Libaries
import pandas as pd
# %% Importing data

encounters = pd.read_csv("data/encounters.csv")

patients = pd.read_csv("data/patients.csv")


# %% Joining datasets
pe = patients.merge(encounters, on = "encounter_id", how="left")

# %% Writing prepared data to disk
pe.to_csv("data/pe.csv")

# %%
