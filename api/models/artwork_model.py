from django.db import models
from django.contrib.auth.models import User
from .arttype_model import ArtType
from .artist_model import Artist
from .condition_model import Condition
from .owner_model import Owner

class Artwork(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
  art_type = models.ForeignKey(ArtType, on_delete=models.CASCADE, related_name='arttype')
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist')
  condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='condition')
  owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner')
  title = models.CharField(max_length=25)
  image_url = models.CharField(max_length=300)
  year_signed = models.CharField(max_length=4)
  location_created = models.CharField(max_length=100)
  size = models.CharField(max_length=10)
  notes = models.CharField(max_length=255)

  class Meta:


  def __str__(self):
    return self.title
