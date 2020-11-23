# %% Libraries
from sys import argv
from sklearn.cluster import KMeans
import seaborn as sns; sns.set()
import data_prep as dp
import pickle as pk
from datetime import date, datetime
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
        kmeans = KMeans(n_clusters = k).fit(data)
        inertia.append(kmeans.inertia_)

    return(inertia)

#### FOR ELBOW EVALUATION
# you can use the code below to see an elbow plot of the clusters
# ! In our testing we found 5 clusters to be ideal.
#
# inertia = eval_k(...)
#sns.lineplot(y = inertia, x = range(1, KMAX+1))
#
# %%

def train_model(patient_data=patient_data, k = 5):

    return(KMeans(n_clusters = k, n_jobs=-1, algorithm = "elkan", n_init = 20).fit(patient_data))
# %%
def export_model():

    d = datetime.today().strftime("%Y_%m_%d_%H:%M:%S")
    model = train_model()
    pk.dump(model, open("models/kmeans"+d+".sav", 'wb'))
    print("Model Exported\nSum of Distances of Samples to Nearest Cluster(s):", (model.inertia_**.5))

export_model()