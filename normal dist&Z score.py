# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:07:56 2019

@author: CADD
"""

import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss

mu=0
variance=1
sigma=math.sqrt(variance)

x=pd.read_csv(r"G:\DATA SCIENCE\Paneer\datas\mtcars.csv")
#print(x)
#y=x.iloc[3,]
#print(y)
#x=np.linspace(-4,4,200)
#print(x)
plt.plot(ss.norm.pdf(x,mu,sigma))
plt.show()




#z score
df=pd.read_csv(r"G:\DATA SCIENCE\Paneer\datas\mtcars.csv")
print(df)
#y=x.iloc[3,]
#print(y)
y=df.mean()
z=df.std()
print(y,z)
score=(df-y)/z
print(score)


s=df.skew()
print(s)
k=df.kurt()
print(k)


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats
data = pd.read_csv(r'G:\DATA SCIENCE\Paneer\datas\Sample.csv')
print(data)
mu=data.mean()
print(mu)
variance=data.var()
print(variance)
sigma=data.std()
print(sigma)
x=np.linspace(mu-5*sigma,mu+5*sigma,200)
print(x)
plt.plot(x,scipy.stats.norm.pdf(x,mu,sigma))
plt.show()
s=data.skew()
print(s)
k=data.kurt()
print(k)

