from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# 1st Variation by using Proxy, just adding additional functionality
class Person(User):
    class Meta:
        proxy = True
        ordering = ('email',)

    def do_something(self):
        pass


# 2nd Variation by using One To One Field, creating new table
class Profile(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        pass

