from rest_framework.generics import (
    ListAPIView
)
from posts.models import Post

from .serializers import (
    PostListSerializer
)

class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()