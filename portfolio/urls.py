from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.index),
    path('categories/', views.categories)
]
