from django.urls import path, include
from . import views

app_name = 'comment'
# if we want to use 'namespace' keyword in our core/urls.py
# we need to define app_name here

urlpatterns = [
    path('create/', views.CommentCreateAPIView.as_view(), name="comment-create"),
    path('list/', views.CommentListAPIView.as_view(), name="comment-list"),
    path('delete/<pk>', views.CommentDeleteAPIView.as_view(), name="comment-delete"),
    path('update/<pk>', views.CommentUpdateAPIView.as_view(), name="comment-update"),
     
]