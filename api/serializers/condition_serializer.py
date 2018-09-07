from rest_framework import serializers
from api.models import *


class ConditionSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Condition
    fields = (
        'id',
        'url',
        'name',
    )
