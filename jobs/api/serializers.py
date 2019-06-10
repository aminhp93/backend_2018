from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField
)

from posts.models import Post

post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail'
)

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    class Meta:
        model = Post
        fields = [
            'id',
            'url',
            'content'
        ]

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
             'id',
            'title', 
            'content',
            'is_done',
            'is_doing',
            'default_cost',
            'actual_cost',
            'timestamp'
        ]
    
class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'content'
        ]