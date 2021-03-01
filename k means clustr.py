# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:43:38 2019

@author: CADD
"""


import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
 
X=np.random.uniform(0,1,1000)

Y=np.random.uniform(0,1,1000)
df_xy=pd.DataFrame(columns=["X","Y"])
df_xy.X=X
df_xy.Y=Y
df_xy
df_xy.plot(x="X",y="Y",kind="scatter")
model1=KMeans(n_clusters=5).fit(df_xy)#model creation
model1.labels_
model1.cluster_centers_
df_xy.plot(x="X",y="Y",c=-model1.labels_,kind="scatter",
    s = 1,cmap=plt.cm.coolwarm)


from sklearn.cluster import KMeans
import numpy as np
data=np.array([[1,2,3,4,5],[1,0,3,2,4],[4,3,23,5,5],[23,4,5,1,4],[23,5,2,3,5]])
labels=np.array([["Flat1"],["Flat2"],["Flat3"],["Flat4"],["Flat5"]])
N_CLUSTERS=3
kmeans=KMeans(init='k-means++',n_clusters=N_CLUSTERS)
kmeans.fit(data)
pred_classes=kmeans.predict(data)
for cluster in range(N_CLUSTERS):
          print('cluster:',cluster)
          print(labels[np.where(pred_classes==cluster)])
