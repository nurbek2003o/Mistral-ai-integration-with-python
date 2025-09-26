# app/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import ChatView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("ask/", ChatView.as_view(), name="ask_view"),
]
