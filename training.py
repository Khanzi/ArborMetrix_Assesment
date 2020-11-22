# %% Libraries
from sys import argv
from sklearn.cluster import KMeans
import seaborn as sns; sns.set()
import data_prep as dp
import os, sys


## GLOBAL VARS

KMAX = 15 # Maximum number of clusters to evaluate


# %% File Path Handling
if len(sys.argv) == 1:
    print("\n No paths to CSVs provided. Defaulting to given data.")
    patients_path = "data/patients.csv"
    encounters_path = "data/encounters.csv"
elif len(sys.argv) == 3:
    print("Attempting to use provided datasets")
    patients_path = sys.argv[1]
    encounters_path = sys.argv[2]
else:
    print("""
    If you wish to provide paths to your own CSV's then:\n
    training.py "path_to_patient_data" "path_to_encounter_data"\n
    """)
    sys.exit("Path Error")

# Importing and Preparing Data
patient_data = dp.prepare_data(patients_path, encounters_path)

# %% Elbow Evaluation

def eval_k(data, kmax = KMAX):
    """Iterates through different cluster numbers and returns a list of 
    the sum squared distances of samples to their closest cluster center.

    Args:
        data (Pandas.DataFrame): DataFrame containing data to be clustered.
        kmax (int): Maximum number of clusters to test.
    """

    inertia = []

    for k in range(1,kmax+1):
        kmeans = KMeans(n_clusters = k, n_jobs=-1).fit(data)
        inertia.append(kmeans.inertia_)

    return(inertia)

def elbow_plot(inertia, kmax = KMAX):
    sns.lineplot(y = inertia, x = range(1, kmax+1))
    
# %%
i = eval_k(patient_data)
elbow_plot(i)
# %%

# %%
