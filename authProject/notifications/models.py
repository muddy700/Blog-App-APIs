from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message