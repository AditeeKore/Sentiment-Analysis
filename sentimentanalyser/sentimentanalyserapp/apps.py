from copyreg import pickle
import os
from django.apps import AppConfig
from django.conf import settings
from numpy import vectorize


class SentimentanalyserappConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    # name = 'sentimentanalyserapp'
    path = os.path.join(settings.MODELS, 'models.pkl')

    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    model = data['model']
    vectorizer = data['vectorizer']
