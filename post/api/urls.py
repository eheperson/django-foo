from django.urls import path, include
from . import views

from django.views.decorators.cache import cache_page

app_name = 'post'
# if we want to use 'namespace' keyword in our core/urls.py
# we need to define app_name here

urlpatterns = [
    # path('list/', views.PostListAPIView.as_view(), name="post-list"),
    path('list/', cache_page(60*1)(views.PostListAPIView.as_view()), name="post-list"), # caching post list api view
    path('list-model/', views.PostListAPIViewModel.as_view(), name="post-list-model"),
    path('detail/<slug>', views.PostDetailAPIView.as_view(), name="post-detail"),
    path('delete/<slug>', views.PostDeleteAPIView.as_view(), name="post-delete"),
    path('update/<slug>', views.PostUpdateAPIView.as_view(), name="post-update"),
    path('create/', views.PostCreateAPIView.as_view(), name="post-create"),
]