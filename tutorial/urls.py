from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'tutorial'

urlpatterns = [
    path('', views.functionBasedView, name='todo-elo'),
    path('submit/',views.submit,name='todo-submit'),
]