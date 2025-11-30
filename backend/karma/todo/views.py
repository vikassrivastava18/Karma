from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .models import Todo
from .serializers import TodoSerializer
# Create your views here.


class ToDoListCreateView(generics.ListCreateAPIView):
    """
        GET - Returns list of todos for the user
        POST - Creates a new Todo for the user
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        # Automatically set the user field to the authenticated user
        request.data['user'] = request.user.id
        return super().post(request, *args, **kwargs)


class ToDoDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
        GET - Returns a single Karma
        PUT - Updates a single Karma
        DELETE - Deletes a single Karma
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def put(self, request, *args, **kwargs):
        if request.data['status'] == 'co':
            request.data['completed_on'] = timezone.now()

        request.data['user'] = request.user.id
        return super().update(request, *args, **kwargs)