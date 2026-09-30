import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("Model/machine_failure_model.pkl")


# Page title
st.title("Industrial Machine Failure Prediction")
st.write("Enter the machine operating details to predict failure risk.")


# User inputs
machine_type = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

air_temperature = st.number_input(
    "Air Temperature [K]",
    min_value=295.3,
    max_value=304.5,
    value=300.0
)

process_temperature = st.number_input(
    "Process Temperature [K]",
    min_value=305.7,
    max_value=313.8,
    value=310.0
)

rotational_speed = st.number_input(
    "Rotational Speed [rpm]",
    min_value=1168,
    max_value=2886,
    value=1500
)

torque = st.number_input(
    "Torque [Nm]",
    min_value=3.8,
    max_value=76.6,
    value=40.0
)

tool_wear = st.number_input(
    "Tool Wear [min]",
    min_value=0,
    max_value=253,
    value=100
)


# Prediction button
if st.button("Predict Failure Risk"):

    machine_data = pd.DataFrame({
        "Type": [machine_type],
        "Air temperature [K]": [air_temperature],
        "Process temperature [K]": [process_temperature],
        "Rotational speed [rpm]": [rotational_speed],
        "Torque [Nm]": [torque],
        "Tool wear [min]": [tool_wear]
    })

    prediction = model.predict(machine_data)
    probability = model.predict_proba(machine_data)[0][1]

    if prediction[0] == 1:
        st.error("⚠️ Machine Failure Risk Detected")
    else:
        st.success("✅ Machine is predicted as Normal")

    st.write(
        "Estimated Failure Probability:",
        round(probability * 100, 2),
        "%"
    )