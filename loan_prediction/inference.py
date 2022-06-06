#!/usr/bin/env python
# coding: utf-8

# In[7]:


from loan_prediction import preprocessing as p
import joblib


# In[8]:


def make_prediction(test):
    test = p.fill_missing(test)
    test = p.model_preprocessing(test)
    model = joblib.load("../models/model")
    Final_prediction = model.predict(test)
    return Final_prediction


# In[ ]:




