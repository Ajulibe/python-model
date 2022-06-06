#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from loan_prediction import preprocessing as p


# In[8]:


def build_model(features):
    target = features[['Loan_Status']]
    features = features.drop(['Loan_Status'], axis=1)
    features_train, features_test, target_train, target_test = p.split_data(features, target)
    features_train = p.fill_missing(features_train)
    features_train = p.model_preprocessing_train(features_train)
    p.add_model(features_train, target_train)
    eva = p.model_evaluation(features_test, target_test)
    return eva
