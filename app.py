import streamlit as st
import pandas as pd

#Input
channel_id = st.text_input('Youtube channel URL', value = '')

#Button
if st.button('Get DATA!'):
    #Run get data function
    pass

df = pd.read_csv('youtubeAnalyticsData.csv')

df
