#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from flask import Flask, render_template, request
import pickle
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')


@app.route('/index.html', methods=['POST', 'GET'])
def sentiment():
    str_features = [str(x) for x in request.form.values()]
        
    score = ((model.polarity_scores(str(str_features))))['compound']    
        
    if (score > 0):
        label = 'This sentence is positive'     
    elif (score == 0):
        label ='This sentence is neutral'
    else:
        label = 'This sentence is negative'

    output = label
    
    return render_template('index.html', prediction_text='{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
