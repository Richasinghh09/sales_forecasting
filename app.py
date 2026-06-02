import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("rf_model_small.pkl")

st.title("Rossmann Sales Forecasting")

store = st.number_input("Store ID", min_value=1, max_value=1115, value=1)

dayofweek = st.selectbox(
    "Day Of Week",
    [1,2,3,4,5,6,7]
)

promo = st.selectbox(
    "Promo",
    [0,1]
)

open_store = st.selectbox(
    "Open",
    [0,1]
)

schoolholiday = st.selectbox(
    "School Holiday",
    [0,1]
)

competitiondistance = st.number_input(
    "Competition Distance",
    value=1000.0
)

if st.button("Predict Sales"):

    data = pd.DataFrame({
        "Store":[store],
        "DayOfWeek":[dayofweek],
        "Open":[open_store],
        "Promo":[promo],
        "StateHoliday":[0],
        "SchoolHoliday":[schoolholiday],
        "StoreType":[0],
        "Assortment":[0],
        "CompetitionDistance":[competitiondistance],
        "CompetitionOpenSinceMonth":[0],
        "CompetitionOpenSinceYear":[0],
        "Promo2":[0],
        "Promo2SinceWeek":[0],
        "Promo2SinceYear":[0],
        "PromoInterval":[0],
        "Year":[2015],
        "Month":[7],
        "Day":[31],
        "WeekOfYear":[31],
        "IsWeekend":[0],
        "IsMonthStart":[0],
        "IsMonthEnd":[1]
    })

    prediction = model.predict(data)

    st.success(
        f"Predicted Sales: {prediction[0]:,.2f}"
    )