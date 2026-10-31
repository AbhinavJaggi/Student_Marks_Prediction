import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.joblib")

st.title("Student Marks Predictor")
st.write("Predict student marks using Machine Learning")

st.success("ML Model Loaded Successfully!")
st.header("Enter Student Details")

hours = st.number_input(
    "Weekly Self Study Hours",
    min_value=0.0,
    max_value=168.0,
    value=20.0
)

attendance = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=85.0
)

participation = st.number_input(
    "Class Participation",
    value=8.0
)
if st.button("Predict Marks"):

    new_student = pd.DataFrame({
        'weekly_self_study_hours': [hours],
        'attendance_percentage': [attendance],
        'class_participation': [participation]
    })

    prediction = model.predict(new_student)[0]

    st.subheader("Prediction Result")
    st.success(f"Predicted Student Score: {prediction:.2f}")