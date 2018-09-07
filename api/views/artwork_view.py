from rest_framework import viewsets
from api.serializers import *
from api.models import *


class ArtworkViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Artworks to be viewed or edited
  """
  queryset = Artwork.objects.all().order_by("title")
  serializer_class = ArtworkSerializer

  def perform_create(self, serializer):
    # Since we don't pass the user info in the POST body from the client app, we add that info here as the argument to our overridden version of the save() method
    serializer.save(user=self.request.user)
    serializer.save(art_type=self.request.user)
    serializer.save(artist=self.request.user)
    serializer.save(condition=self.request.user)
    serializer.save(owner=self.request.user)
