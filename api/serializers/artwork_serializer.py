from rest_framework import serializers
from api.models import *
from .user_serializer import UserSerializer
from .arttype_serializer import ArtTypeSerializer
from .artist_serializer import ArtistSerializer
from .condition_serializer import ConditionSerializer
from .owner_serializer import OwnerSerializer


class ArtworkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.url')
    art_type = serializers.ReadOnlyField(source='art_type.name')
    artist_first = serializers.ReadOnlyField(source='artist.first_name')
    artist_last = serializers.ReadOnlyField(source='artist.last_name')
    condition = serializers.ReadOnlyField(source='condition.name')
    owner_first = serializers.ReadOnlyField(source='owner.first_name')
    owner_last = serializers.ReadOnlyField(source='owner.last_name')

    class Meta:
        model = Artwork
        fields = (
            'id',
            'url',
            'user',
            'art_type',
            'artist_first',
            'artist_last',
            'condition',
            'owner_first',
            'owner_last',
            'title',
            'image_url',
            'year_signed',
            'location_created',
            'size',
            'notes',
        )
