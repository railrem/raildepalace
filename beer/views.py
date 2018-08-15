# Create your views here.

from beer.models import Beer
from beer.serializers import BeerSerializer
from rest_framework import generics
class BeerListCreate(generics.ListCreateAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer