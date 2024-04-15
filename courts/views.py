from rest_framework import generics
from .models import Court
from .serializers import CourtSerializer

class CourtListCreateView(generics.ListCreateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

class CourtRetrieveView(generics.RetrieveAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer