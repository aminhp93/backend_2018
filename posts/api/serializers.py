from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField
)

from posts.models import Post

class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = []