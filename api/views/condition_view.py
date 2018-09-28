from rest_framework import viewsets
from api.serializers import *
from api.models import *

class ConditionViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Conditions to be viewed or edited
  """
  queryset = Condition.objects.all().order_by("name")
  serializer_class = ConditionSerializer


