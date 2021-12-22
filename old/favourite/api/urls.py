from django.urls import path, include
from . import views


app_name = 'favourite'
# if we want to use 'namespace' keyword in our core/urls.py
# we need to define app_name here

urlpatterns = [
    path('list-create/', views.FavouriteListCreateAPIView.as_view(), name="favourite-list-create"),
    path('retrieve-update/<pk>', views.FavouriteRetrieveUpdateAPIView.as_view(), name="favourite-retrieve-update"),
    path('retrieve-destroy/<pk>', views.FavouriteRetrieveDestroyAPIView.as_view(), name="favourite-retrieve-destroy"),
    path('retrieve-update-destroy/<pk>', views.FavouriteRetrieveUpdateDestroyAPIView.as_view(), name="favourite-retrieve-update-destroy"),
]