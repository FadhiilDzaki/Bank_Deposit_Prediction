import streamlit as st
import eda
import prediction

# navigation
navigation = st.sidebar.selectbox('Halaman: ',('Predictor', 'Data Analysis'))

# page
if navigation == 'Predictor':
    prediction.run()
else:
    eda.run()

    