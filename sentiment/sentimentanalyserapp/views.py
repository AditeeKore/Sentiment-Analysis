from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from matplotlib.pyplot import text
from djangorestframework import APIView
from sentimentanalyser import sentimentanalyserapp
from sentimentanalyser.sentimentanalyserapp.apps import SentimentanalyserappConfig
from .models import SentimentModel
from .forms import SentimentForm
from code import SentimentAnalyzer

# Create your views here.
def home(request):
    form = SentimentForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            sent = form.cleaned_data.get('Sentence')    # got the sentence
            textAns = SentimentAnalyzer(sent)
            context['text'] = textAns
        else:
            form = SentimentForm()
    
    context['form'] = form
    return render(request, 'home.html', context=context)

class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            text = request.GET.get('text')

            vector = SentimentanalyserappConfig.vectorizer.transform({text})

            prediction = SentimentanalyserappConfig.model.predict(vector)[0]

            response = {'text_sentiment': prediction}

            return JsonResponse(response)
