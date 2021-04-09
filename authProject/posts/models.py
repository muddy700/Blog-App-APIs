from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.CharField(max_length=500, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.title