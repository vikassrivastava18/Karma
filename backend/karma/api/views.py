from django.utils import timezone
from django.utils.timezone import localdate

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import generics

from .models import Karma, Todo, Reflection
from .serializers import KarmaSerializer, ReflectionSerializer, TodoSerializer

# Get today's date based on the timezone in settings.py


class KarmaListView(generics.ListCreateAPIView):
    """
        GET - Returns a list of all karmas
        POST - Creates a new Karma
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Karma.objects.all()
    serializer_class = KarmaSerializer

    def get_queryset(self):
        today = localdate()
        return Karma.objects.filter(date=today, user=self.request.user)

    def post(self, request, *args, **kwargs):
        # Automatically set the user field to the authenticated user
        request.data['user'] = request.user.id
        return super().post(request, *args, **kwargs)


class KarmaDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Karma.objects.all()
    serializer_class = KarmaSerializer


class ToDoListView(generics.ListCreateAPIView):
    """
        GET - Returns list of todos
        POST - Creates a new Todo
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


class ToDoDetailView(generics.RetrieveUpdateDestroyAPIView):
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


class ReflectionView(generics.ListCreateAPIView):
    """
        GET - Returns a list of all reflections
        POST - Creates a new reflection
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer

    def get_queryset(self):
        return Reflection.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        # Automatically set the user field to the authenticated user
        request.data['user'] = request.user.id
        return super().post(request, *args, **kwargs)

