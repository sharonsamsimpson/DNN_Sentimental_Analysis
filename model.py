#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import nltk

nltk.download('vader_lexicon')

text ="This is a very nice day"

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

score = ((sid.polarity_scores(str(text))))['compound']

pickle.dump((sid), open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))

