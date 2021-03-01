# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:29:44 2019

@author: LIVE WIRE
"""

import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
wc=pd.read_csv(r"G:\DATA SCIENCE\Paneer\datas\mtcars.csv")
wc.columns

#linear
model=smf.ols("mpg~cyl",data=wc).fit()
model.summary()
pred=model.predict({'cyl':10})
pred

plt.plot(wc.cyl,wc.mpg,"bo")
plt.show()

plt.scatter(wc.cyl,wc.mpg,  color='gray')
plt.plot(wc.cyl,pred, color='red', linewidth=2)
plt.show()

#multi linear

model1=smf.ols("mpg~wt+hp+disp",data=wc).fit()
model1.summary()

pred1=model1.predict({'wt': 3.102, 'hp': 152, 'disp':138.2})
pred1


