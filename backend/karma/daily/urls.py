from django.urls import path
from .views import (DailyListCreateView,
                    DailyDetailUpdateDestroyView,
                    ReflectionView)


urlpatterns = [
    path('todos', DailyListCreateView.as_view(), name='tasks'),
    path('todos/<int:pk>', DailyDetailUpdateDestroyView.as_view(), name='task'),
    path('reflections', ReflectionView.as_view(), name='todos'),
]
