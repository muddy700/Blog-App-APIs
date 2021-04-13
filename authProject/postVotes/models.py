from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from posts.models import Post
from django.contrib.postgres.fields import ArrayField

class PostVote(models.Model):
    up = ArrayField(models.CharField(max_length=10), )
    down = ArrayField(models.CharField(max_length=10))
    # userIds = ArrayField(models.CharField(max_length=10))
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
 
    def __str__(self):
        return " Vote For Post # %s" % (self.post)