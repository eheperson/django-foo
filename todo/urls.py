from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'todo'
urlpatterns = [
    path('elo/', views.elo, name='todo-elo'),
    path('submit/',views.submit,name='todo-submit'),
    path('delete/<int:id>/',views.delete,name='todo-delete'),
    path('list/',views.list,name='todo-list'),
    path('sortdata/',views.sortdata,name='todo-sortdata'),
    path('searchdata/',views.searchdata,name='todo-searchdata'),
    path('edit/<int:id>/',views.edit,name='todo-edit'),
    path('update/<int:id>/',views.update,name='todo-update')

]