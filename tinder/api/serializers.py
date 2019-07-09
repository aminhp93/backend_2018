from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField
)

from tinder.models import Tinder

tinder_detail_url = HyperlinkedIdentityField(
    view_name='tinder-api:detail'
)

class TinderListSerializer(ModelSerializer):
    url = tinder_detail_url
    class Meta:
        model = Tinder
        fields = [
            'id',
            'user_id',
            'url',
            'content',
        ]

class TinderDetailSerializer(ModelSerializer):
    class Meta:
        model = Tinder
        fields = [
            'id',
            'user_id',
        ]
    
class TinderCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Tinder
        fields = [
            'user_id',
            'content'
        ]