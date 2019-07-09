from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)
from rest_framework.mixins import DestroyModelMixin

from tinder.models import Tinder

from .serializers import (
    TinderListSerializer,
    TinderDetailSerializer,
    TinderCreateUpdateSerializer
)

from .pagination import TinderPageNumberPagination


class TinderListAPIView(ListAPIView):
    serializer_class = TinderListSerializer
    queryset = Tinder.objects.all()
    pagination_class = TinderPageNumberPagination


class TinderDetailAPIView(RetrieveAPIView):
    serializer_class = TinderDetailSerializer
    queryset = Tinder.objects.all()
    # lookup_field = 'id'


class TinderCreateAPIView(CreateAPIView):
    serializer_class = TinderCreateUpdateSerializer
    queryset = Tinder.objects.all()


class TinderUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = TinderCreateUpdateSerializer
    queryset = Tinder.objects.all()


class TinderDestroyAPIView(DestroyAPIView):
    serializer_class = TinderDetailSerializer
    queryset = Tinder.objects.all()

class TinderDestroyAllAPIView(DestroyModelMixin):
    queryset = Tinder.objects.all()
    serializer_class = TinderDetailSerializer
