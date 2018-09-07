from django.contrib.auth.models import User
from api.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email')
