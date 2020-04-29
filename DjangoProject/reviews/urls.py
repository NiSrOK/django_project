from django.conf.urls import url, include
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from reviews.models import Data

urlpatterns = [
   path('', views.index),
   path('create/', views.create),
   path('edit/<int:id>/', views.edit),
   path('delete/<int:id>/', views.delete),
]