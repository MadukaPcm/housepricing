from django.urls import path
from . import views

urlpatterns = [
    path('', views.PredictionPageView, name='PredictionPage_url'),
]