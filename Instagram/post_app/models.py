from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    image = models.ImageField(default="default-post.png", upload_to='profile_pics')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.author} Post'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
