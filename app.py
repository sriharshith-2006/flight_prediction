import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
    page_title="Flight Price Predictor",
    page_icon="✈️",
    layout="wide"
)

model = pickle.load(open("model.pkl", "rb"))
ohe = pickle.load(open("one_hot.pkl", "rb"))
oe = pickle.load(open("oe.pkl", "rb"))
st.sidebar.title("✈️ Flight Price Prediction")
page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔮 Predict Price",
        "ℹ️ About Project"
    ]
)
if page == "🏠 Home":

    st.title("✈️ Flight Price Prediction")

    st.markdown("""
    ### Welcome!

    Predict airline ticket prices using Machine Learning.

    #### Features
    - Airline Selection
    - Source & Destination
    - Stops Information
    - Journey Details
    - Instant Price Prediction

    ---
    Developed using:
    - Python
    - Scikit-Learn
    - Streamlit
    """)

# --------------------------
# ABOUT PAGE
# --------------------------

elif page == "ℹ️ About Project":

    st.title("ℹ️ About Project")

    st.markdown("""
    ### Flight Price Prediction System

    This project predicts airline ticket prices based on:

    - Airline
    - Source
    - Destination
    - Total Stops
    - Journey Date
    - Departure Time
    - Arrival Time
    - Duration

    ### ML Techniques

    - One Hot Encoding
    - Ordinal Encoding
    - Regression Model

    ### Author

    Sriharshith
    AI & Data Science Student
    """)

# --------------------------
# PREDICTION PAGE
# --------------------------

elif page == "🔮 Predict Price":

    st.title("🔮 Predict Flight Price")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        airline = st.selectbox(
            "Airline",
            list(ohe.categories_[0])
        )

        source = st.selectbox(
            "Source",
            list(ohe.categories_[1])
        )

        stops = st.selectbox(
            "Total Stops",
            [
                "non-stop",
                "1 stop",
                "2 stops",
                "3 stops",
                "4 stops"
            ]
        )

        date = st.number_input(
            "Journey Date",
            1,
            31
        )

        month = st.number_input(
            "Journey Month",
            1,
            12
        )

    with col2:

        destination = st.selectbox(
            "Destination",
            list(ohe.categories_[2])
        )

        dep_hour = st.number_input(
            "Departure Hour",
            0,
            23
        )

        dep_minute = st.number_input(
            "Departure Minute",
            0,
            59
        )

        arrival_hour = st.number_input(
            "Arrival Hour",
            0,
            23
        )

        arrival_minute = st.number_input(
            "Arrival Minute",
            0,
            59
        )

    duration_min = st.number_input(
        "Duration (Minutes)",
        min_value=0
    )

    st.write("")
    st.write("")

    if st.button(
        "Predict Price",
        use_container_width=True
    ):

        cat_df = pd.DataFrame({
            "Airline":[airline],
            "Source":[source],
            "Destination":[destination]
        })

        ohe_data = ohe.transform(
            cat_df
        ).toarray()

        stop_df = pd.DataFrame({
            "Total_Stops":[stops]
        })

        stop_encoded = oe.transform(
            stop_df
        )

        numerical_features = np.array([[
            date,
            month,
            2025,
            arrival_hour,
            arrival_minute,
            dep_hour,
            dep_minute,
            duration_min
        ]])

        final_input = np.concatenate(
            (
                ohe_data,
                stop_encoded,
                numerical_features
            ),
            axis=1
        )

        prediction = model.predict(
            final_input
        )

        st.success(
            f"💰 Predicted Flight Price: ₹{prediction[0]:,.2f}"
        )

        st.balloons()