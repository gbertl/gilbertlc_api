from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects),
    path('projects/<int:pk>/', views.project_detail),
    path('categories/', views.categories),
    path('technologies/', views.technology_list),
    path('screenshots/', views.screenshot_list)
]
