from django.contrib import admin
from .models import Post, Profile
# Register your models here.

admin.site.register(Post) # register post model to admin page

admin.site.register(Profile) # register profile model to admin page