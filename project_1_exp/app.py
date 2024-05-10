import streamlit as st
import numpy as np
# from sklearn.preprocessing import StandardScaler
import joblib

# scaler = StandardScaler()

st.set_page_config(layout="wide")

st.title("Resturan Rating Preprocessing App")

st.caption("This app helps you predict a resturant review class")

st.divider()

# inputs that our models takes
averagecost = st.number_input("Please enter the estimated averge cost for two", min_value=50,max_value=999999,value=1000,step=200)

tablebooking = st.selectbox("Resturant has table booking?",["Yes","No"])

onlinedelivery = st.selectbox("Resturants has online booking?",["Yes","No"]) 

pricerange = st.selectbox("What is the price range (1 Gheapest, 4 Most Expensive)",[1,2,3,4])

predict_button = st.button("Predict the reviews!")

st.divider()