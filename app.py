import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("chennai_price_model.pkl","rb"))
columns = pickle.load(open("columns.pkl","rb"))

st.title("Chennai House Price Predictor")

sqft = st.number_input("Area (sqft)", 500, 5000)
bhk = st.number_input("BHK", 1, 5)

location = st.text_input("Location")

if st.button("Predict Price"):
    
    new_house = pd.DataFrame(0, index=[0], columns=columns)

    new_house["area_sqft"] = sqft
    new_house["bhk"] = bhk

    loc_col = "location_" + location

    if loc_col in new_house.columns:
        new_house[loc_col] = 1

    price = model.predict(new_house)[0]

    st.success(f"Estimated Price: {round(price,2)} Lakhs")