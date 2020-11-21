# %% Libaries
from pydoc import describe
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
# %% Importing data

encounters = pd.read_csv("../data/encounters.csv")

patients = pd.read_csv("../data/patients.csv")


# %% Joining datasets
pe = patients.merge(encounters, on = "encounter_id", how="left")
pe.head()
# %%
pe = pd.get_dummies(pe, columns = ["icd10_code"], prefix = [""])
# %%
pe = pe.drop("line_number", axis=1)

pe.set_index('ssn')
# %%
pt = pe.groupby("encounter_id").max()

# %%

#pe.to_csv("data/pe.csv", index= False)
# %%
pc = pe.drop(['encounter_id'], axis = 1)
# %%
pc = pc.set_index('ssn')
# %%
pc
# %%

km = KMeans(n_clusters = 3)
# %%
km.fit_predict(pc)
# %%
centers = km.cluster_centers_
# %%
plt.scatter(centers[:,0], centers[:,1], c='black', s=200, alpha=0.2)
# %%
centers
# %%
pred = km.predict(pc)
# %%
pred
# %%
pe['cluster'] = pred
# %%
pe_peak = pe.sample(10)
# %%
pe['line_number'] = pe['line_number'].astype('int')
# %%
sns.displot(pe, x = "line_number")
# %%
import scipy.cluster.hierarchy as sch
# %%
dendro = sch.dendrogram(sch.linkage(pt, method = "ward"))
# %%
from sklearn.cluster import AgglomerativeClustering

# %%
ag = AgglomerativeClustering(n_clusters = 8)
# %%
# %%
clusters = ag.fit_predict(pt)
# %%
pt['cluster'] = clusters
# %%
pt_peak = pt.sample(100)
# %%
sns.displot(data = pt, x = "cluster")

# %%
