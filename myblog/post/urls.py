from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('query/',views.query,name="query")
]
