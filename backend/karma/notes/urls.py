from django.urls import path
from .views import (NoteCreateListView, NoteDetailView,
                    ImageUploadView, TopicListView,
                    TopicDetailView, TopicNotes)

urlpatterns = [
    path('', NoteCreateListView.as_view(), name='note-list-create'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('topic/<int:topic_id>/', TopicNotes.as_view(), name='topic-notes'),
    path('upload-image/', ImageUploadView.as_view(), name='upload-image'),
    path('topics/', TopicListView.as_view(), name='topics-list'),
    path('topics/<int:pk>', TopicDetailView.as_view(), name='topics-detail')
]