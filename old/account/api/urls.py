from django.urls import path, include
from account.api.views import(
    ProfileView,
    UpdatePassword,
    CreateUserView
)

app_name = 'account'
# if we want to use 'namespace' keyword in our core/urls.py
# we need to define app_name here

urlpatterns = [
    path('me', ProfileView.as_view(), name='account-me'),
    path('change-password/', UpdatePassword.as_view(), name='account-change-password'),
    path('create-user/', CreateUserView.as_view(), name='account-create-user')
]