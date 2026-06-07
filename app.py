import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Rossmann Sales Forecasting", layout="centered")

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "rf_model_small.pkl")

@st.cache_resource(show_spinner=False)
def load_model():
    return joblib.load(model_path)

st.title("🏪 Rossmann Sales Forecasting")
st.markdown("---")

# Input Section
st.subheader("📊 Enter Store Details")

col1, col2 = st.columns(2)

with col1:
    store = st.number_input("Store ID", min_value=1, max_value=1115, value=1)
    dayofweek = st.selectbox("Day Of Week", [1, 2, 3, 4, 5, 6, 7], format_func=lambda x: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][x-1])
    promo = st.selectbox("Promotion", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

with col2:
    open_store = st.selectbox("Store Open", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    schoolholiday = st.selectbox("School Holiday", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    competitiondistance = st.number_input("Competition Distance (meters)", value=1000.0, min_value=0.0)

st.markdown("---")

# Prediction Button
if st.button("🎯 Predict Sales", use_container_width=True):
    try:
        if not os.path.exists(model_path):
            st.error(f"❌ Model file not found at: {model_path}")
            st.stop()

        with st.spinner("Loading forecasting model..."):
            model = load_model()

        data = pd.DataFrame({
            "Store": [store],
            "DayOfWeek": [dayofweek],
            "Open": [open_store],
            "Promo": [promo],
            "StateHoliday": [0],
            "SchoolHoliday": [schoolholiday],
            "StoreType": [0],
            "Assortment": [0],
            "CompetitionDistance": [competitiondistance],
            "CompetitionOpenSinceMonth": [0],
            "CompetitionOpenSinceYear": [0],
            "Promo2": [0],
            "Promo2SinceWeek": [0],
            "Promo2SinceYear": [0],
            "PromoInterval": [0],
            "Year": [2015],
            "Month": [7],
            "Day": [31],
            "WeekOfYear": [31],
            "IsWeekend": [0],
            "IsMonthStart": [0],
            "IsMonthEnd": [1]
        })

        prediction = model.predict(data)
        predicted_sales = prediction[0]

        # Display Results
        st.markdown("---")
        st.subheader("✅ Prediction Result")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Store ID", store)
        with col2:
            st.metric("Day of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][dayofweek-1])
        with col3:
            st.metric("Competition Distance", f"{competitiondistance:.0f}m")

        st.success(f"## 🎯 Predicted Sales: **€{predicted_sales:,.2f}**")

        # Additional Details
        st.info(f"""
        **Prediction Details:**
        - Store Status: {'Open' if open_store == 1 else 'Closed'}
        - Running Promotion: {'Yes' if promo == 1 else 'No'}
        - School Holiday: {'Yes' if schoolholiday == 1 else 'No'}
        """)

    except Exception as e:
        st.error(f"❌ Prediction Error: {str(e)}")
        st.error("Please check your inputs and try again.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
    <p>Rossmann Sales Forecasting Model | Random Forest Prediction</p>
    <p>Built with Streamlit • Deployed on Railway</p>
</div>
""", unsafe_allow_html=True)
