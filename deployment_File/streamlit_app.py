import streamlit as st
import eda
import prediction

st.set_page_config(
    page_title = 'Coffee beans roast level Predictor',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

page = st.sidebar.selectbox('Select page : ', ('EDA', 'Prediction'))

if page == 'EDA':
    eda.run()

else:
    prediction.run()