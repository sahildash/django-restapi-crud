from rest_framework import generics

from .models import Particulars
from .serializers import ParticularsSerializer


class ParticularsList(generics.ListAPIView):
    queryset = Particulars.objects.all()
    serializer_class = ParticularsSerializer


class ParticularsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Particulars.objects.all()
    serializer_class = ParticularsSerializer