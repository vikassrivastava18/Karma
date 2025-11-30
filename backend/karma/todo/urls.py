from django.urls import path
from .views import ToDoListCreateView, ToDoDetailUpdateDestroyView

urlpatterns = [
    path('todos', ToDoListCreateView.as_view(), name='todos'),
    path('todos/<int:pk>', ToDoDetailUpdateDestroyView.as_view(), name='todo'),
]
