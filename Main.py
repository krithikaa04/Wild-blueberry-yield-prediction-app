import pickle
import time

import numpy as np
import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Wild Blueberry Yield Prediction", page_icon="🫐")
st.sidebar.write('**DEVELOPED BY** ')
st.sidebar.write('GS Prethika (21PD08)')
st.sidebar.write('Krithika L (21PD19)')


# Define the main content layout
st.markdown(
    """
    <style>
        body {
        background-color: #6DA9E5;
    }
    .header {
        font-size: 36px;
        font-weight: bold;
        color: #0A66C2;
        text-align: center;
        margin-top: 20px;
        justify-content: center;
    }

        .sub-header {
            font-size: 20px;
            color: #333333;
            text-align: center;
            margin-top: 10px;
        }

        .description {
            font-size: 18px;
            color: #fffff;
            text-align: center;
            margin-top: 20px;
            font-weight: bold;
        }

        .app-image {
            display: block;
            margin: 20px auto;
        }

        .app-button {
            font-size: 18px;
            background-color: #0A66C2;
            color: #FFFFFF;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            text-align: center;
            margin-top: 20px;
        }

        .app-button:hover {
            background-color: #0954A0;
        }
        .blueberry-icon {
        color: #0A66C2;
        font-size: 40px;
        vertical-align: middle;
        margin-right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main header
st.write('<div class="header"><i class="fas fa-seedling blueberry-icon"></i> Wild Blueberry Yield Prediction</div>', unsafe_allow_html=True)

# Description
st.write('<div class="description">Welcome to our Wild Blueberry Yield Prediction app. ',unsafe_allow_html=True)
st.write('<div class="description">This app uses machine learning concepts to predict wild blueberry yields based on various features like temperature, rainfall etc',unsafe_allow_html=True)
st.write('<div class="description">Get accurate predictions to optimize your crop management.',unsafe_allow_html=True)
# App image
st.image("https://www.thespruce.com/thmb/0k8tYA_KxsO4IMlmiep1KclB2UQ=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/blueberries-vaccinium-spp-3269245-01-42fb9fde200d4c05a2a5d3c6e94a0bf2.jpg", caption="Blueberry prediction", use_column_width=True)

