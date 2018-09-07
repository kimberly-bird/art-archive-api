from rest_framework import serializers
from api.models import *


class OwnerSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Owner
    fields = (
        'id',
        'url',
        'first_name',
        'last_name',
        'current_location',
    )
