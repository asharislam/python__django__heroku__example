from os import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('home/', views.HomeView.as_view(), name="home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contract/', views.ContractView.as_view(), name="contract")
]
