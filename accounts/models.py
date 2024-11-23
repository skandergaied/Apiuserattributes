from django.db import models
from django.contrib.auth.models import User, Group

class UserAttribute(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='attributes')
    attributes = models.JSONField(default=list)

    def __str__(self):
        return f"{self.user.username}'s attributes"

class UserGroup(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(UserAttribute)