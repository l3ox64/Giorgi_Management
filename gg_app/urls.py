# django_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('register/', views.sign_up, name='register'),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]