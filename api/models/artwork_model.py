from django.db import models
from django.contrib.auth.models import User
from .arttype_model import ArtType
from .artist_model import Artist
from .condition_model import Condition
from .owner_model import Owner

class Artwork(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artwork')
  art_type = models.ForeignKey(ArtType, on_delete=models.CASCADE, related_name='artwork')
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artwork')
  condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='artwork')
  owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='artwork')
  title = models.CharField(max_length=25)
  image_url = models.CharField(max_length=300)
  year_signed = models.CharField(max_length=4)
  location_created = models.CharField(max_length=100)
  size = models.CharField(max_length=10)
  notes = models.CharField(max_length=255)

  def __str__(self):
    return self.title
