from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView
)
from posts.models import Post

from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateUpdateSerializer
)

class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    # lookup_field = 'id'

class PostCreateAPIView(CreateAPIView):
    serializer_class = PostCreateUpdateSerializer
    queryset = Post.objects.all()

class PostUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PostCreateUpdateSerializer
    queryset = Post.objects.all()

class PostDestroyAPIView(DestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()

