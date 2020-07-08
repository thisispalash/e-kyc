from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
  path('upload/', TemplateView.as_view()),
]