from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:num1>/', views.group_posts),
] 
