import streamlit as st
import pickle
import pandas as pd
import numpy as np
# import sklearn

model=pickle.load(open("pre.pkl","rb"))
k=pd.read_csv("man.csv")
def predict_price(location,sqft,bath,bhk):
    loc_index=np.where(k.columns==location)[0][0]
    x=np.zeros(len(k.columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    return model.predict([x])[0]

st.title("House Price Prediction")
location=st.selectbox("Loction Name",k.columns[3:].values)
total_sqft=st.number_input("Enter Total Square feet")
bathroom=st.number_input("Enter Total Numbers of Bathrooms")
bhk=st.number_input("Enter BHK")

if st.button("Predict Price"):
    result=predict_price(location,total_sqft,bathroom,bhk)
    st.subheader(result)

