from django.db.models import Prefetch
from rest_framework import generics
from rest_framework.permissions import *

from .serializers import *


# Create your views here.

class TodoListAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoIncompleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TodoGetSerializer

    def get_queryset(self):
        return TodoList.objects.all().prefetch_related(
            Prefetch('tasks', queryset=Task.objects.filter(mark=False)))


class TodoCompleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TodoGetSerializer

    def get_queryset(self):
        return TodoList.objects.all().prefetch_related(
            Prefetch('tasks', queryset=Task.objects.filter(mark=True)))


class TaskListAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
