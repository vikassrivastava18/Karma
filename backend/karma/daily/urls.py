from django.urls import path
from .views import (DailyListCreateView,
                    DailyDetailUpdateDestroyView,
                    ReflectionView, add_daily_data)

urlpatterns = [
    path('', DailyListCreateView.as_view(), name='daily-list-create'),
    path('<int:pk>', DailyDetailUpdateDestroyView.as_view(), name='daily-detail-update'),
    path('add-data/<int:days>', add_daily_data, name='add-daily-data'),
    path('reflections', ReflectionView.as_view(), name='todos'),
]
