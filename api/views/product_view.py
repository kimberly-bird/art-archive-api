from rest_framework import viewsets
from api.serializers import *
from api.models import *

class ProductTypeViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows ProductTypes to be viewed or edited
  """
  queryset = ProductType.objects.all().order_by("title")
  serializer_class = ProductTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Products to be viewed or edited
  """
  queryset = Product.objects.all().order_by("title")
  serializer_class = ProductSerializer
