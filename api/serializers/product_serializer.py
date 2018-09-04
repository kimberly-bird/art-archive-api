from rest_framework import serializers
from api.models import *
from . import customer_serializer

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ProductType
    fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
  # customer = customer_serializer.CustomerSerializer(read_only=True)

  class Meta:
    model = Product
    fields = (
        'id',
        'url',
        # 'customer',
        'product_type',
        'title',
        'description',
        'price',
        'quantity',
    )
