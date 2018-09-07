from rest_framework import serializers
from api.models import *


class ArtistSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Artist
    fields = (
        'id',
        'url',
        'first_name',
        'last_name',
        'dob',
        'death_date',
    )
