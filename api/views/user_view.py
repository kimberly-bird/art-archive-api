from django.contrib.auth.models import User
from rest_framework import viewsets
from django.core import serializers

from api.models import *
from api.serializers import *


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
