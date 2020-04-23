from django.urls import path, include
from django.contrib import admin
from django.conf import settings

from pagina import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contato/', views.contato, name="contato"),
]