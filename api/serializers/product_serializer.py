from rest_framework import serializers
from api.models import *

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ProductType
    fields = '__all__'
