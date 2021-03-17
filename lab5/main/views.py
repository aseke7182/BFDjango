from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from rest_framework import generics, viewsets
from rest_framework.permissions import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q, Prefetch
import copy


# Create your views here.

class TodoListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoIncompleteRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TodoGetSerializer

    def get_queryset(self):
        return TodoList.objects.all().prefetch_related(
            Prefetch('tasks', queryset=Task.objects.filter(mark=False)))


class TodoCompleteRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TodoGetSerializer

    def get_queryset(self):
        return TodoList.objects.all().prefetch_related(
            Prefetch('tasks', queryset=Task.objects.filter(mark=True)))


class TaskListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
