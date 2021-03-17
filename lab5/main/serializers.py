from rest_framework import serializers
from .models import *


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'created', 'due_on', 'owner', 'mark',)


class TodoGetSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ('id', 'name', 'tasks')


