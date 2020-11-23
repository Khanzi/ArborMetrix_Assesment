# %%
import pandas as pd 
import pickle as pk
from sklearn.cluster import KMeans
import data_prep as dp
import sys, os 
from datetime import datetime

# %% File Path Handling
if len(sys.argv) == 1:
    print("\n No paths to CSVs provided. Defaulting to given data.")
    patients_path = "data/patients.csv"
    encounters_path = "data/encounters.csv"
    model_path = "models/kmeans2020_11_22_13:49:49.sav"
elif len(sys.argv) == 4:
    print("Attempting to use provided datasets")
    patients_path = sys.argv[1]
    encounters_path = sys.argv[2]
    model_path == sys.argv[3]
else:
    print("""
    If you wish to provide paths to your own CSV's then:\n
    training.py "path_to_patient_data" "path_to_encounter_data" "path_to_model" \n"
    """)
    sys.exit("Path Error")


patient_data = dp.prepare_data(patients_path, encounters_path)
model = pk.load(open(model_path, 'rb'))

# %%
def label_clusters(patient_data = patient_data, model = model):

    patient_data['cluster'] = model.predict(patient_data)
    patient_data.reset_index(inplace=True)

    return(patient_data[['ssn','cluster']])

# %%
def save_cluster_results():

    d = datetime.today().strftime("%Y_%m_%d_%H:%M:%S")
    data = label_clusters()
    data.to_csv("clustered_patients"+d+".csv", index=False)

save_cluster_results()