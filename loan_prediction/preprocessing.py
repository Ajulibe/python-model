#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# In[36]:


def model_preprocessing_train(feature):
    feature = feature.replace({'Dependents':'3+'},'0')
    feature['TotalIncome']=feature['ApplicantIncome']+feature['CoapplicantIncome']
    feature=feature.drop(['Loan_ID','ApplicantIncome','CoapplicantIncome'],axis=1)
    numerical_feature = get_numerical_features(feature)
    categorical_feature = get_categorical_features(feature)
    add_encoder(categorical_feature)
    categorical_feature = encode(categorical_feature)
    feature = concate_num_cat(categorical_feature, numerical_feature)
    feature = feature_selection(feature)
    add_scaler(feature)
    feature = scale(feature)
    return feature


# In[37]:


def add_model(feature, target):
    model=KNeighborsClassifier(n_neighbors=5)
    model.fit(feature,target.values.ravel())
    joblib.dump(model,'../models/model')


# In[38]:


def scale(features):
    scale_feature=joblib.load('../models/scaler')
    features = scale_feature.transform(features)
    return features


# In[39]:


def add_scaler(feature):
    scale= StandardScaler()
    scale.fit(feature)
    joblib.dump(scale,'../models/scaler')


# In[40]:


def feature_selection(feature):
    feature =feature[['Self_Employed','Property_Area','TotalIncome','Loan_Amount_Term','Credit_History']]
    return feature


# In[41]:


def concate_num_cat(categorical_feature, numerical_feature):
    categorical_feature.index = numerical_feature.index
    feature = pd.concat([categorical_feature, numerical_feature], axis=1)
    return feature


# In[42]:


def encode(categorical_feature):
    encode=joblib.load('../models/encoder')
    categorical_feature = encode.transform(categorical_feature)
    categorical_feature = pd.DataFrame(categorical_feature, columns = ['Gender','Married','Education','Self_Employed','Property_Area'])
    return categorical_feature


# In[43]:


def add_encoder(categorical_feature):
    encode=OrdinalEncoder(handle_unknown='use_encoded_value',unknown_value=5)
    encode.fit(categorical_feature)
    joblib.dump(encode,'../models/encoder')


# In[44]:


def get_numerical_features(feature):
    numerical_feature=feature[['LoanAmount','TotalIncome','Dependents','Loan_Amount_Term','Credit_History']]
    return numerical_feature


# In[45]:


def get_categorical_features(feature):
    categorical_feature=feature[['Gender','Married','Education','Self_Employed','Property_Area']]
    return categorical_feature


# In[46]:


def fill_missing(features):
    features['LoanAmount']=features['LoanAmount'].fillna(features['LoanAmount'].mean())
    features['Self_Employed']=features['Self_Employed'].fillna('No')
    features['Gender']=features['Gender'].fillna('Male')
    features['Dependents']=features['Dependents'].fillna("0")
    features['Married']=features['Married'].fillna('yes')
    features['Loan_Amount_Term']=features['Loan_Amount_Term'].fillna("360.0")
    features['Credit_History']=features['Credit_History'].fillna("1.0")
    return features


# In[47]:


def split_data(features, target):
    features_train, features_test, target_train, target_test= train_test_split(features,target,random_state=42,test_size=0.33)
    return features_train, features_test, target_train, target_test


# In[48]:


def model_preprocessing(feature):
    feature = feature.replace({'Dependents':'3+'},'0')
    feature['TotalIncome']=feature['ApplicantIncome']+feature['CoapplicantIncome']
    feature = feature.drop(['Loan_ID','ApplicantIncome','CoapplicantIncome'],axis=1)
    numerical_feature = get_numerical_features(feature)
    categorical_feature = get_categorical_features(feature)
    categorical_feature = encode(categorical_feature)
    feature = concate_num_cat(categorical_feature, numerical_feature)
    feature = feature_selection(feature)
    feature = scale(feature)
    return feature


# In[49]:


def compute_accuracy(target_test, target_prediction):
    return accuracy_score(target_test, target_prediction)


# In[50]:


def model_evaluation(feature_test, target_test):
    feature_test = fill_missing(feature_test)
    feature_test= model_preprocessing(feature_test)
    Knnmodel=joblib.load('../models/model')
    y_pred=Knnmodel.predict(feature_test)
    target_prediction = pd.DataFrame(y_pred,columns=['Loan_status'])
    rmse=compute_accuracy(target_test,target_prediction)
    return rmse


# In[ ]:




