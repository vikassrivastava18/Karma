from django.urls import path
from .views import ToDoListCreateView, ToDoListCreateView

urlpatterns = [
    path('todos', ToDoListCreateView.as_view(), name='todos'),
    path('todos/<int:pk>', ToDoListCreateView.as_view(), name='todo'),
]
