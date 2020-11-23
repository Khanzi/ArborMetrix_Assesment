# %% Libaries
from pydoc import describe
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core import algorithms
from scipy.cluster.hierarchy import dendrogram, linkage
import seaborn as sns; sns.set()
import scipy.cluster.hierarchy as sch
from sklearn import cluster
# %% Importing data

encounters = pd.read_csv("../data/encounters.csv")

patients = pd.read_csv("../data/patients.csv")


# %% Joining datasets
pe = patients.merge(encounters, on = "encounter_id", how="left")
pe.head()
# %%
pe = pd.get_dummies(pe, columns = ["icd10_code"], prefix = [""])
pe.head()
# %%
pe = pe.drop("line_number", axis=1)

#pe.set_index('ssn')
# %%
pt = pe.groupby(['ssn']).sum()
pt.describe()
# %%
#rawr = pt.sample(100)
# %%
dendro = sch.dendrogram(sch.linkage(pt, method = "ward"))
# %%
kmeans = cluster.KMeans(n_clusters = 4, max_iter = 600, verbose = 1, n_jobs = -1, algorithm = 'elkan', n_init = 100)
# %%
clusters = kmeans.fit_predict(pt)
# %%
sns.displot(clusters)

# %%
def eval_k(data, kmax):

    inertia = []

    for k in range(1,kmax+1):
        kmeans = cluster.KMeans(n_clusters = k, n_jobs=-1).fit(data)
        inertia.append(kmeans.inertia_**0.5)

    return(inertia)






# %%
inertia = eval_k(pt, 15)

# %%
fig = sns.lineplot(y = inertia, x = range(1, 16))
plt.xlabel("Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Evaluation")
# %%
kmeans.inertia_ ** 0.5
# %%
