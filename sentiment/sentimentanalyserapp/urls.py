from django.urls import path
from sentimentanalyserapp import views

urlpatterns = [path("" ,views.home, name="home"),]