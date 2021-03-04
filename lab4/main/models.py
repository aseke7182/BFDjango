from django.db import models
import datetime


# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    due_on = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=2))
    owner = models.CharField(max_length=200)
    mark = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='task')
