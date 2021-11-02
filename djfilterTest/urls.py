from django.urls import path, include
from . import views

app_name = 'djfiltertest'

urlpatterns = [
    path('', views.BootstrapFilterView, name='bootstrap')
]