from django.urls import path
from .views import NoteCreateListView, NoteDetailView, ImageUploadView


urlpatterns = [
    path('notes/', NoteCreateListView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('upload-image/', ImageUploadView.as_view(), name='upload-image'),
]