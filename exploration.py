# %%
import pandas as pd
import numpy as np 
from pandas_profiling import ProfileReport
# %% Import dataframes

#encounters = pd.read_csv("data/encounters.csv")

patients = pd.read_csv("data/patients.csv")

# %% Profiling

#profile_encounters = ProfileReport(encounters, title = "Encounters Summary", explorative = True)

profile_patients = ProfileReport(patients, title = "Patients Summary", explorative = True)

#profile_encounters.to_file("Encounters.html")
profile_patients.to_file("Patients.html")
# %%


