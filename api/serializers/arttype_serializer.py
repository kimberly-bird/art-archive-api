from rest_framework import serializers
from api.models import *


class ArtTypeSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = ArtType
    fields = (
        'id',
        'url',
        'name',
    )
