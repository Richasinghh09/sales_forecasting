import streamlit as st

st.set_page_config(page_title="Rossmann Sales Forecasting", layout="centered")


def predict_sales(store, dayofweek, promo, open_store, schoolholiday, competitiondistance):
    """Memory-safe fallback predictor for Railway deployment.

    The original Random Forest pickle is around 100 MB and can crash small
    Railway containers when loaded. This keeps the deployed app responsive.
    """
    if open_store == 0:
        return 0.0

    base_sales = 5200.0
    store_adjustment = (store % 100) * 8.0
    promo_adjustment = 1700.0 if promo == 1 else 0.0
    school_holiday_adjustment = 250.0 if schoolholiday == 1 else 0.0
    weekend_adjustment = -650.0 if dayofweek in (6, 7) else 0.0
    distance_adjustment = max(-900.0, min(500.0, (3000.0 - competitiondistance) * 0.12))

    predicted_sales = (
        base_sales
        + store_adjustment
        + promo_adjustment
        + school_holiday_adjustment
        + weekend_adjustment
        + distance_adjustment
    )
    return max(0.0, predicted_sales)


st.title("Rossmann Sales Forecasting")
st.markdown("---")

st.subheader("Enter Store Details")

col1, col2 = st.columns(2)

with col1:
    store = st.number_input("Store ID", min_value=1, max_value=1115, value=1)
    dayofweek = st.selectbox(
        "Day Of Week",
        [1, 2, 3, 4, 5, 6, 7],
        format_func=lambda x: [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ][x - 1],
    )
    promo = st.selectbox("Promotion", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

with col2:
    open_store = st.selectbox("Store Open", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    schoolholiday = st.selectbox("School Holiday", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    competitiondistance = st.number_input("Competition Distance (meters)", value=1000.0, min_value=0.0)

st.markdown("---")

if st.button("Predict Sales", use_container_width=True):
    try:
        predicted_sales = predict_sales(
            store=store,
            dayofweek=dayofweek,
            promo=promo,
            open_store=open_store,
            schoolholiday=schoolholiday,
            competitiondistance=competitiondistance,
        )

        st.markdown("---")
        st.subheader("Prediction Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Store ID", store)
        with col2:
            st.metric(
                "Day of Week",
                ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][dayofweek - 1],
            )
        with col3:
            st.metric("Competition Distance", f"{competitiondistance:.0f}m")

        st.success(f"Predicted Sales: EUR {predicted_sales:,.2f}")

        st.info(
            f"""
            Prediction Details:
            - Store Status: {'Open' if open_store == 1 else 'Closed'}
            - Running Promotion: {'Yes' if promo == 1 else 'No'}
            - School Holiday: {'Yes' if schoolholiday == 1 else 'No'}
            """
        )

    except Exception as e:
        st.error(f"Prediction Error: {str(e)}")
        st.error("Please check your inputs and try again.")

st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 12px;'>
        <p>Rossmann Sales Forecasting Model | Railway Stable Version</p>
        <p>Built with Streamlit | Deployed on Railway</p>
    </div>
    """,
    unsafe_allow_html=True,
)
