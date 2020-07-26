from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers

from . import views

urlpatterns = [
  # path('upload/', TemplateView.as_view()),
  path('persons', views.person_list),
  path('docs', views.document_list),
  path('persons/<key>', views.person_info),  
]