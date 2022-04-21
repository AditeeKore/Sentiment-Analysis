import imp
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np



st.title('Sentiment Analysis for Social Media')
st.markdown('This application is about analysing sentiments of texts.')

st.sidebar.title('Sentiment Analysis')

data = pd.read_csv('Tweets.csv')

if st.checkbox('Show Data'):
    st.write(data.head(8))

st.sidebar.subheader('Actions')
sentiment = st.sidebar.radio('Sentiment Type', ('positive', 'negative', 'neutral'))
st.write(data.query('airline_sentiment==@sentiment')[['text']].sample(1).iat[0,0])
st.write(data.query('airline_sentiment==@sentiment')[['text']].sample(1).iat[0,0])
st.write(data.query('airline_sentiment==@sentiment')[['text']].sample(1).iat[0,0])

select=st.sidebar.selectbox('Visualisation of Data',['Histogram', 'Pir Chart'], key=1)

sentiment_visualise = data['airline_sentiment'].value_counts()
sentiment_visualise = pd.DataFrame({'Sentiment':sentiment_visualise.index,'Text':sentiment_visualise})
st.markdown('### Sentiment count')

if select == 'Histogram':
    fig = px.bar(sentiment_visualise, x='Sentiment', y='Text', color='Text', height=500)
    st.plotly_chart(fig)
else:
    fig = px.pie(sentiment_visualise, values='Text', names='Sentiment')
    st.plotly_chart(fig)
