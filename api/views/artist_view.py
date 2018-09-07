from rest_framework import viewsets
from api.serializers import *
from api.models import *

class ArtistViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Artists to be viewed or edited
  """
  queryset = Artist.objects.all().order_by("title")
  serializer_class = ArtistSerializer


