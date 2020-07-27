from django.urls import include, path
from rest_framework import routers

from . import views

urlpatterns = [
  path('persons', views.PersonView.as_view()),
  path('person/<key>/',views.PersonView.as_view()),
  path('docs/', views.DocumentView.as_view()),
  
  path('login/', views.LoginView.as_view()),
]