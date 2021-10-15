from django.urls import path, include
from . import views

app_name = 'post'
# if we want to use 'namespace' keyword in our core/urls.py
# we need to define app_name here

urlpatterns = [
    path('list/', views.PostListAPIView.as_view(), name="api-list"),
    path('list-model/', views.PostListAPIViewModel.as_view(), name="api-post-list-model"),
    path('detail/<slug>', views.PostDetailAPIView.as_view(), name="api-post-detail"),
    path('delete/<slug>', views.PostDeleteAPIView.as_view(), name="api-post-delete"),
    path('update/<slug>', views.PostUpdateAPIView.as_view(), name="api-post-update"),
    path('create/', views.PostCreateAPIView.as_view(), name="api-post-create"),
]