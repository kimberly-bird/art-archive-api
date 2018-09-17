from rest_framework import viewsets
from api.serializers import *
from api.models import *

class ArtTypeViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows ArtTypes to be viewed or edited
  """
  queryset = ArtType.objects.all().order_by("name")
  serializer_class = ArtTypeSerializer


