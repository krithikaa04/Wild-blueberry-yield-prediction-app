import pickle

import numpy as np
import streamlit as st

# Load the pre-trained model from a pickle file
with open('C:\Users\Krithika\Desktop\PSG\SEM5\ml\Wild-blueberry-yield-prediction-app\catboost.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title(' Wild Blueberry Yield Prediction App')

# Define input parameters
input_data = {
    'Unnamed: 0':0,
    'Row#':40,
    'clonesize': st.number_input('Clone Size', min_value=0.0, value=0.0),
    'honeybee': st.number_input('Honeybee', min_value=0.0, value=0.0),
    'bumbles': st.number_input('Bumbles', min_value=0.0, value=0.0),
    'andrena': st.number_input('Andrena', min_value=0.0, value=0.0),
    'osmia': st.number_input('Osmia', min_value=0.0, value=0.0),
    'MaxOfUpperTRange': st.number_input('Max Of Upper Temperature Range', min_value=0.0, value=0.0),
    'RainingDays': st.number_input('Raining Days', min_value=0.0, value=0.0),
    'fruitset': st.number_input('Fruitset', min_value=0.0, value=0.0),
}

if st.button('Predict'):
    # Convert input data to a list and predict yield
    input_values = list(input_data.values())
    predicted_value = model.predict([input_values])[0]
    st.success(f'Predicted Yield: {predicted_value:.2f}')
