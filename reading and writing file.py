# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:35:37 2019

@author: LIVE WIRE
"""

import csv
with open('r') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)
        
import csv
 
myData = [["first_name", "second_name", "Grade"],
          ['A', 'B', 'C'],
          ['D', 'E', 'F']]
 
myFile = open(r'G:\DATA SCIENCE\Paneer\datas, 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")


import csv
 
results = []
with open(r'G:\DATA SCIENCE\Paneer\datas.csv','r') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    print(results)
    
import csv
 
with open(r'G:\DATA SCIENCE\Paneer\datas', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
    writer.writerow({'Grade': 'A', 'first_name': 'Rachael',
                     'last_name': 'Rodriguez'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})
 
print("Writing complete")







#Append rows to existing file
import csv
with open(r'E:\Rani DS\New folder\beneficiary.csv','w') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow(['user_id','beneficiary'])
    newFileWriter.writerow([1,'xyz'])
    newFileWriter.writerow([2,'pqr'])
    
import csv
with open(r'E:\Rani DS\New folder\beneficiary.csv','r') as newFile:
    newFileReader = csv.reader(newFile)
    for row in newFileReader:
        print(row)


import csv
with open(r'E:\Rani DS\New folder\beneficiary.csv', 'a') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow([3, 'xxx'])
    newFileWriter.writerow([4, 'yyy'])
    newFileWriter.writerow([5, 'zzz'])