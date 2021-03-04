from django.shortcuts import render
from .models import *
import json


# Create your views here.
def uncompleted(request, pk):
    todo = TodoList.objects.get(id=pk)
    tasks = Task.objects.filter(todo_list__id=pk, mark=False)
    context = {
        'todo': todo,
        'tasks': tasks
    }
    return render(request, 'index.html', context)


def completed(request, pk):
    todo = TodoList.objects.get(id=pk)
    tasks = Task.objects.filter(todo_list__id=pk, mark=True)
    context = {
        'todo': todo,
        'tasks': tasks
    }
    return render(request, 'completed.html', context)
