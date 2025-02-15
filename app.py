import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

st.markdown(
    '<h1 style="text-align: center; color: white;">House Price Prediction App</h1>',unsafe_allow_html=True
)

with open ( r'dt.pkl','rb') as f:
    dt=pickle.load(f)
with open(r'lr.pkl','rb') as f:
    lr=pickle.load(f)
with open(r'kn.pkl','rb') as f:
    kn=pickle.load(f)

#['SquareFeet', 'Bedrooms', 'Bathrooms', 'Neighborhood', 'YearBuilt','Price'],

sf=st.number_input('Area(SquareFeet)',max_value=2999,min_value=1000)
br=st.number_input('Bedrooms',min_value=2, max_value=5)
ba=st.number_input('Bathrooms',min_value=1, max_value=3)
#map({'Rural':0,'Suburb':1,'Urban':2})
nh=st.selectbox('Neighbourhood',['Rural','Suburb','Urban'])
y=st.number_input('YearBuilt',min_value=1900,max_value=2021)

if nh=='Rural':
    nh=0
elif nh=='Suburb':
    nh=1
else:
    nh=2

if st.button('Predict'):
    x=np.array([[sf,br,ba,nh,y]])
    lr_pred=lr.predict(x)
    kn_pred=kn.predict(x)
    dt_pred=dt.predict(x)
    st.write('Linear Regression Prediction (More accurate): ',round(lr_pred[0],2))
    st.write('KNN Prediction: ',round(kn_pred[0],2))
    st.write('Decision Tree Prediction: ',round(dt_pred[0],2))
