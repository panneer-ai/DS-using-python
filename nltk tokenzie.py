# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 06:07:42 2020

@author: SANGAR LOCAL
"""

import nltk
#nltk.download()
paragraph= """ India is an agricultural country. Most of the people live in villages and are farmers.
          They grow cereals, pulses, vegetables and fruits. The farmers lead a tough life.
          They get up early in the morning and go to the fields. They stay and work on the farm late till evening.
          The farmers usually live in kuchcha houses. Though, they work hard they remain poor.
          Farmers eat simple food; wear simple clothes and rear animals like cows, buffaloes and oxen. 
          Without them there would be no cereals for us to eat.
          They play an important role in the growth and economy of a country """
 
#tokenize  sentence
sentences =nltk.sent_tokenize(paragraph)

#tokenize the words
words =nltk.word_tokenize(paragraph)

          
          