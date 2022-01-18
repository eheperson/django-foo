
from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.TestView.as_view(), name='app-index')
]