from django.utils.timezone import localdate
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication,
                                           BasicAuthentication)

from .models import DailyKarma, Reflection
from .serializers import (DailyKarmaSerializer,
                          ReflectionSerializer)
# Create your views here.


class DailyListCreateView(generics.ListCreateAPIView):
    """
        GET - Returns a list of all karmas
        POST - Creates a new Karma
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DailyKarma.objects.all()
    serializer_class = DailyKarmaSerializer

    def get_queryset(self):
        today = localdate()
        return DailyKarma.objects.filter(date=today, user=self.request.user)

    def post(self, request, *args, **kwargs):
        # Automatically set the user field to the authenticated user
        request.data['user'] = request.user.id
        return super().post(request, *args, **kwargs)


class DailyDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DailyKarma.objects.all()
    serializer_class = DailyKarmaSerializer


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