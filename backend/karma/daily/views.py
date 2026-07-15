from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)

from .models import DailyKarma, Reflection
from .serializers import (DailyKarmaSerializer,
                          ReflectionSerializer)
from utils.add_data import SaveData


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
        today = timezone.now().date()
        return DailyKarma.objects.filter(date=today, user=self.request.user)

    def post(self, request, *args, **kwargs):
        # Automatically set the user field to the authenticated user
        request.data['user'] = request.user.id
        return super().post(request, *args, **kwargs)


class DailyDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
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


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_daily_data(request, days):
    try:
        if not request.user.is_superuser:
            raise PermissionDenied("Only superuser can access this API.")

        username = "vikas"
        save_data = SaveData(username, days)
        save_data.add_data()
        return Response({"message": "Data added successfully"})

    except Exception as e:
        return Response(
            {"message": f"Data save failed due to {e}"},
            status=500
        )

