# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:57:32 2019

@author: LIVE WIRE
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
customer_data = pd.read_csv(r"G:\DATA SCIENCE\Paneer\datas\hierarchical-clustering.csv")
customer_data
customer_data.shape
data = customer_data.iloc[:, 3:5].values
import scipy.cluster.hierarchy as shc

plt.figure(figsize=(10, 7))
plt.title("Customer Dendograms")
dend = shc.dendrogram(shc.linkage(data, method='ward'))# linkage ward-variants of distances between the clusters.

#After knowing cluster value using dendogram
from sklearn.cluster import AgglomerativeClustering

cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster.fit_predict(data)

plt.figure(figsize=(10, 7))
plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow')





import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
x= np.array([[5,3],
    [10,15],
    [15,12],
    [24,10],
    [30,30],
    [85,70],
    [71,80],
    [60,78],
    [70,55],
    [80,91]])
from sklearn.cluster import AgglomerativeClustering as ac
#help(ac)
cluster=ac(n_clusters=2,affinity='euclidean',linkage='ward')
cluster.fit_predict(x)                  #lnkage=grp obj into hierarichal cluter tree
print(cluster.labels_)
plt.scatter(x[:,0],x[:,1],c=cluster.labels_)
plt.show()