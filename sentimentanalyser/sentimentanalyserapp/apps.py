import joblib
import os
from django.apps import AppConfig
from django.conf import settings
from numpy import vectorize


class SentimentanalyserappConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    # name = 'sentimentanalyserapp'
    path = 'C:/Users/Aditee/OneDrive/Documents/GitHub/Sentiment-Analysis/sentimentanalyser/models.p'

    with open(path, 'rb') as joblibmodel:
        data = joblib.load(joblibmodel)
    model = data['model']
    vectorizer = data['vectorizer']
