# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:47:32 2019
      
@author: User
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS  
#text = 'all your base are belong to us all of your base base base'
text = 'Rahul Gandhi is an Indian politician and a member of the Indian Parliament, representing the constituency of Wayanad, Kerala in the 17th Lok Sabha. A member of the Indian National Congress, he served as the President of the Indian National Congress from 16 December 2017 to 3 July 2019. Wikipedia'
def generate_wordcloud(text): # optionally add: stopwords=STOPWORDS and change the arg below
    wordcloud = WordCloud().generate(text)# set or space-separated string
    plt.imshow(wordcloud)   #display an image
    plt.axis("off")
    plt.show()

generate_wordcloud(text)

    
