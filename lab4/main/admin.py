from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ('mark',)
    list_display = ('name', 'created', 'due_on', 'owner', 'mark')
    search_fields = ['name', 'owner']


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', ]
