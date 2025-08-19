import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("🔍 Breast Cancer Diagnosis Prediction")
st.write("Enter the tumor characteristics to predict if it's **Malignant** or **Benign**.")

# Input fields for the features
concave_points_worst = st.number_input("Concave Points (Worst)", min_value=0.0, step=0.0001)
perimeter_worst = st.number_input("Perimeter (Worst)", min_value=0.0, step=0.01)
radius_worst = st.number_input("Radius (Worst)", min_value=0.0, step=0.01)
area_worst = st.number_input("Area (Worst)", min_value=0.0, step=0.1)
concavity_worst = st.number_input("Concavity (Worst)", min_value=0.0, step=0.0001)

# Predict button
if st.button("Predict Diagnosis"):
    # Arrange input into numpy array
    input_data = np.array([[concave_points_worst, perimeter_worst, radius_worst, area_worst, concavity_worst]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    if prediction == 1:  # assuming 1 = Malignant, 0 = Benign
        st.error("⚠️ Diagnosis: Malignant")
    else:
        st.success("✅ Diagnosis: Benign")
