from rest_framework import viewsets
from api.serializers import *
from api.models import *


class ArtworkViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Artworks to be viewed or edited
  """
  queryset = Artwork.objects.all().order_by("id")
  serializer_class = ArtworkSerializer

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)
    serializer.save(art_type=self.request.art_type)
    serializer.save(artist=self.request.artist)
    serializer.save(condition=self.request.condition)
    serializer.save(owner=self.request.owner)
