# %% Libraries
import pandas as pd
import os, sys


def prepare_data(p, e):
    """Imports and prepares data for KMeans

    Args:
        p (string): Path to patients csv
        e (string): Path to encounters csv
    """

    # Importing data
    encounters = pd.read_csv(e)
    patients = pd.read_csv(p)

    # Joining Data
    pe = patients.merge(encounters, on = "encounter_id", how="left")

    # Pivoting codes to one-hot encoded vars
    pe = pd.get_dummies(pe, columns = ["icd10_code"], prefix = [""])
    pe = pe.drop("line_number", axis=1)

    # Aggregating by patient
    pt = pe.groupby(['id']).sum()

    return(pt)

    