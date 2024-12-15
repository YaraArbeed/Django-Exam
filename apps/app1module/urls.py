from django.urls import path, include
from apps.app1module import views

urlpatterns = [
  path('Home Page', views.Home_Page, name='Home_Page'),  # Landing Page
   path('List Games', views.List_Games, name='List_Games'),  # List_Games


]
