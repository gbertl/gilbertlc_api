from . import views
from django.urls import path

urlpatterns = [
    path('projects/', views.index),
    path('projects/<int:id>/', views.project_detail),
]
