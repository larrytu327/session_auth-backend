from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ##on_delete CASCADE, if the profile is deleted, than everything under it gets deleted
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    type  = models.CharField(max_length=255, default='')
    parents = models.CharField(max_length=255, default='')
    students = models.CharField(max_length=255, default='')
    teachers = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.first_name