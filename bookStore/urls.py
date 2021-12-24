from django.urls import path, include
from . import views

app_name = 'bookStore'

urlpatterns = [
    path('', views.BootstrapFilterView, name='bootstrap')
]