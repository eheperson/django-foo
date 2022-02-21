from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog-post-detail', kwargs={'pk':self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='profilePics/default.jpeg', upload_to='profilePics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self):
        super().save()

        img = Image.open(self.img.path)

        if img.height > 300 or img.width > 300:
            outputImgSize = (300, 300)
            img.thumbnail(outputImgSize)
            img.save(self.img.path) 