#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from flask import Flask, render_template, request, jsonify
import pickle
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')


@app.route('/index.html', methods=['POST', 'GET'])
def sentiment():
    
    text = request.form['text']
    
    nltk.download('vader_lexicon')
    
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    
    score = ((sid.polarity_scores(str(text)))['compound'])

    if(score>0):
        label = 'This sentence is positive'
    elif(score == 0):
        label = 'This sentence is neutral'
    else:
        label = 'This sentence is negative'
        
    output = label
    
    return render_template('index.html', prediction_text='{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
