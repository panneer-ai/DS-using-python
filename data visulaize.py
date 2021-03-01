# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:19:31 2019

@author: CADD
"""
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt      #import matplotlib.pyplot as plt
t=[1,4,5,6,7,8,9]
s=[1,2,3,4,5,6,7]

plt.plot(t,s,'g',label='line 1')
plt.plot([6,7,8],[9,10,11],'b',label='line 2',linewidth=2)#g-c-colors
plt.title('Chart')                                      #label-axis name
plt.xlabel('Xaxis')
plt.ylabel('Yaxis')
plt.grid(True,color='r')                #grid displays
plt.legend()                                    #display label axis name
plt.show()

#bar
from matplotlib import pyplot as plt
#plt.bar([0.5,1.5,2.85,4.0,6.0],[40,50,70,80,90],label='bmw',width=0.5)
plt.hist([.75,1.75,3.2,4.50,4.75],[60,20,40,80,50],label='audi',width=1)
plt.title(' bar Chart')                                      #label-axis name
plt.xlabel('Xaxis')
plt.ylabel('Yaxis')
plt.legend()                                    #display label axis name in chart
plt.show()







#histogram
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(r"G:\DATA SCIENCE\Paneer\datas\Sample.csv")
df
plt.hist(df['Marks'],['Attendance'])
plt.title('Age distribution')
plt.xlabel('marks')
plt.ylabel('attedance')
plt.legend()
plt.show()


#pie chart
from matplotlib import pyplot as plt
lab='python','c++','ruby','java'
sizes = 215,130,245,210
cols = ('c','m','r','b')
plt.pie(sizes,labels=lab,explode=(0,0,0.2,0), colors=cols,startangle = 140,autopct='%0.2f%%',shadow=False)
plt.tittle('pie')
plt.show()

help(plt.pie)
#scatter 
from matplotlib import pyplot as plt
x=[1,2,3,1,5,5,1,8,2,3,3,3,6]
y=[7,7,5,6,1,5,2,5,3,6,4,6,6]  
x1=[4,5,4,5,8,6,4,8,2,5,0]
y1=[6,8,9,9,8,6,5.2,3.2,5,6,0]
plt.scatter(x,y,label='high',color='r')
plt.scatter(x1,y1,label='low',color='g')
plt.title('scatter Chart')                                      #label-axis name
plt.xlabel('Xaxis')
plt.ylabel('Yaxis')
plt.legend()                                    #display label axis name in chart
plt.show()
