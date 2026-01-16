import logging
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note, UploadedImage, NoteTopic
from .serializers import (NoteSerializer,
                          UploadedImageSerializer, TopicSerializer)

logger = logging.getLogger(__name__)


class NoteCreateListView(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by('-updated_at')
    serializer_class = NoteSerializer


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class ImageUploadView(APIView):
    # Accepts multipart/form-data with a field 'file'
    def post(self, request, format=None):
        try:
            file_obj = request.FILES.get('file')
            if not file_obj:
                return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
            img = UploadedImage.objects.create(file=file_obj)
            serializer = UploadedImageSerializer(img, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            logger.error(f"Error occurred in image upload: {e}")
            return Response({'error': 'Image upload failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TopicListView(generics.ListCreateAPIView):
    queryset = NoteTopic.objects.all()
    serializer_class = TopicSerializer