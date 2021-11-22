from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='catalog-index'),
    path('books/', views.BookListView.as_view(), name='catalog-books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='catalog-book-detail'),
]


