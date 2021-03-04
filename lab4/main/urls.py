from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.uncompleted),
    path('<int:pk>/completed/', views.completed)
]
