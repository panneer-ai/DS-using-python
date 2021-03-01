# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 06:27:03 2020

@author: SANGAR LOCAL
"""

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph = """ India is an agricultural country. Most of the people live in villages and are farmers.
          They grow cereals, pulses, vegetables and fruits. The farmers lead a tough life.
          They get up early in the morning and go to the fields. They stay and work on the farm late till evening.
          The farmers usually live in kuchcha houses. Though, they work hard they remain poor.
          Farmers eat simple food; wear simple clothes and rear animals like cows, buffaloes and oxen. 
          Without them there would be no cereals for us to eat.
          They play an important role in the growth and economy of a country """
          
#tokenize  sentence
sentences =nltk.sent_tokenize(paragraph)
stemmer=PorterStemmer()

#stemming
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words1 = []
    for word in words:
        if word not in set(stopwords.words("english")):
            words1.append(stemmer.stem(word))
     
    sentences[i] = ' '.join(words1)     
          