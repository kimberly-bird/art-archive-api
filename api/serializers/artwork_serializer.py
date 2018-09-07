from rest_framework import serializers
from api.models import *
from .user_serializer import User
from .arttype_serializer import ArtType
from .artist_serializer import Artist
from .condition_serializer import Condition
from .owner_serializer import Owner


class ArtworkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.url')
    art_type = serializers.ReadOnlyField(source='art_type.url')
    artist = serializers.ReadOnlyField(source='artist.url')
    condition = serializers.ReadOnlyField(source='condition.url')
    owner = serializers.ReadOnlyField(source='owner.url')

    class Meta:
        model = Artwork
        fields = (
            'id',
            'url',
            'name',
            'user',
            'art_type',
            'artist',
            'condition',
            'owner',
            'title',
            'image_url',
            'year_signed',
            'location_created',
            'size',
            'notes',
        )
