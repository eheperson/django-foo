"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# that imports are required for staticfiles and mediafiles
from django.conf import settings
from django.conf.urls.static import static

# from djfilterTest.views import BootstrapFilterView

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
    path('api/post/', include('post.api.urls', namespace='post')),
    path('api/comment/', include('comment.api.urls', namespace='comment')),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('lab/', include('lab.urls', namespace='lab')),
    path('djfiltertest/', include('djfilterTest.urls', namespace='djfiltertest')),
    path('api/favourite/', include('favourite.api.urls', namespace='favourite')),
    path('api/user/', include('account.api.urls', namespace='account')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # do not forget define a MEDIA_URL variable in the settings.py
