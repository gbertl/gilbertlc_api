from . import views
from django.urls import path

urlpatterns = [
    path('projects/', views.project_list),
    path('projects/<int:id>/', views.project_detail),
    path('technologies/', views.technology_list),
    path('categories/', views.category_list),
    path('screenshots/', views.screenshot_list),
]
