#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

url = 'http://localhost:5000/predict_api' 
r = requests.post(url, json={'text':'string'})

print(r.json())

