# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:44:11 2019

@author: CADD
"""
#wrd count

import re
input_str = 'Box A contains 3 red and 5 white balls, while Box B contains 4 red & 2 blue balls.'
result = re.sub(r'\d+', '', input_str)
print(result)


import nltk
#nltk.download()
from nltk.corpus import stopwords
senten="This is an example showing off stop word"
stop_words=set(stopwords.words("english"))
print(stop_words)
 




#stem
from nltk.stem import PorterStemmer
ewords=["wait","waiting","waited","waits"]
ps=PorterStemmer()
for w in ewords:
    rootWord=ps.stem(w)
    print(rootWord)
    
    
    
from nltk.stem import PorterStemmer
import pandas as pd
ewords=pd.read_csv(r"E:\Rani DS\New folder\stem.csv")
ewords
ps=PorterStemmer()
for w in ewords:
    rootWord=ps.stem(w)
    print(rootWord)
    
#tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
sentence="Hai ,you have a good knowledge in python,I am visiting your sites"
words=word_tokenize(sentence)
print(words)
ps=PorterStemmer()
for w in words:
    rootWord=ps.stem(w)
    print(rootWord)
    
#word count
import pandas as pd
train = pd.read_csv(r'E:\Rani DS\New folder\movie.csv')
train['word_count'] = train['pc'].apply(lambda x: len(str(x).split(" ")))
print(train[['pc','word_count']])

#no of characters
import pandas as pd
train = pd.read_csv(r'E:\Rani DS\New folder\movie.csv')
train['char_count'] = train['pc'].str.len() ## this also includes spaces
print(train[['pc','char_count']])


import pandas as pd
from nltk.corpus import stopwords
train = pd.read_csv(r'E:\Rani DS\New folder\movie.csv')
stop = stopwords.words('english')
train['stopwords'] = train['pc'].apply(lambda x: len([x for x in x.split() if x in stop]))
print(train[['pc','stopwords']])

#special char
import pandas as pd
train = pd.read_csv(r'E:\Rani DS\New folder\movie.csv')
train['hastags'] = train['pc'].apply(lambda x: len([x for x in x.split() if x.endswith('%')]))
print(train[['pc','hastags']])

#numerics
import pandas as pd
train = pd.read_csv(r'E:\Rani DS\New folder\movie.csv')
train['numerics'] = train['pc'].apply(lambda x: len([x for x in x.split() if x.isdigit()]))
print(train[['pc','numerics']])







    
    
    