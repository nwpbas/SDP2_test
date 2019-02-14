from django.urls import path
from . import views

app_name = "multiplication"
urlpatterns = [
    path('', views.index, name='index'),
    path('input/', views.index, name='input'),
    path('stat/', views.stat, name='stat'),
]