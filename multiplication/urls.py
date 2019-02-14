from django.urls import path
from . import views

app_name = "multiplication"
urlpatterns = [
    path('', views.index, name='index'),
]