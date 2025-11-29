from django.urls import path
from .views import (DailyListCreateView,
                    DailyDetailUpdateDestroyView,
                    ReflectionView)


urlpatterns = [
    path('daily', DailyListCreateView.as_view(), name='tasks'),
    path('daily/<int:pk>', DailyDetailUpdateDestroyView.as_view(), name='task'),
    path('reflections', ReflectionView.as_view(), name='todos'),
]
