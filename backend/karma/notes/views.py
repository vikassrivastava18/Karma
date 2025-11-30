from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note, UploadedImage
from .serializers import NoteSerializer, UploadedImageSerializer


class NoteCreateListView(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by('-updated_at')
    serializer_class = NoteSerializer


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class ImageUploadView(APIView):
    # Accepts multipart/form-data with a field 'file'
    def post(self, request, format=None):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        img = UploadedImage.objects.create(file=file_obj)
        serializer = UploadedImageSerializer(img, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)