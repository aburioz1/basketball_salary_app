import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import sklearn
import pickle
basketball_model = pickle.load(open("C:\\Users\\HP\\Downloads\\randomf_model.sav", "rb"))
st.title("BasketBall Salary App")
image = Image.open('C:\\Users\\HP\\Downloads\\pexels-cottonbro-studio-6767231.jpg')
st.image(image, width= 350)
def user_report():
    rating = st.number_input('rating: ',min_value=0)
    jersey = st.number_input('jersey: ',min_value=0)
    team = st.number_input('team: ',min_value=0)
    position = st.number_input('position: ',min_value=0)
    status = st.selectbox("country: ",['Australia','Canada','Others','USA'])
    if (status == 'Australia'):
        country = 0
    elif (status == 'Canada'):
        country = 1
    elif (status == 'Others'):
        country = 2
    else:
        country = 3
    draft_year = st.number_input('draft_year: ',min_value=0)
    draft_round = st.number_input('draft_round: ',min_value=0)
    draft_peak = st.number_input('draft_peak: ',min_value=0)
    data_report = {
        'rating': rating,
        'jersey': jersey,
        'team': team,
        'position': position,
        'country': country,
        'draft_year': draft_year,
        'draft_round': draft_round,
        'draft_peak': draft_peak

    }
    data = pd.DataFrame(data_report, index=[0])
    return data
user_data = user_report()
st.write(user_data)
prediction = basketball_model.predict(user_data)
st.success(prediction)


