from rest_framework import serializers
from api.models import *
from .user_serializer import UserSerializer
from .arttype_serializer import ArtTypeSerializer
from .artist_serializer import ArtistSerializer
from .condition_serializer import ConditionSerializer
from .owner_serializer import OwnerSerializer


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
