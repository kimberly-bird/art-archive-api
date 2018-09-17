from rest_framework import viewsets
from api.serializers import *
from api.models import *

class OwnerViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Owners to be viewed or edited
  """
  queryset = Owner.objects.all().order_by("first_name")
  serializer_class = OwnerSerializer


