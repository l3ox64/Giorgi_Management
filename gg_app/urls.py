# django_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]