%%writefile app.py
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'knn_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

# Create a title for your app
st.title("Monthly Revenue Prediction App")

# Create input fields for the user to enter the features
st.header("Enter Customer Features:")
# Replace 'feature1', 'feature2', etc. with the actual names of your features
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
# Add more input fields as needed

# Create a button to trigger the prediction
if st.button("Predict Monthly Revenue"):
  # Create a DataFrame with the user input
  input_data = pd.DataFrame([[feature1, feature2]], columns=['feature1', 'feature2'])  # Replace with your actual feature names

  # Make a prediction using the loaded model
  prediction = loaded_model.predict(input_data)

  # Display the prediction
  st.header("Predicted Monthly Revenue:")
  st.write(prediction[0])