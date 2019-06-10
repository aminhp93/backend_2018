from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView
)
from stocks.models import Stock

from .serializers import (
    StockListSerializer,
    StockDetailSerializer,
    StockCreateUpdateSerializer
)

from .pagination import StockPageNumberPagination


class StockListAPIView(ListAPIView):
    serializer_class = StockListSerializer
    queryset = Stock.objects.all()
    pagination_class = StockPageNumberPagination


class StockDetailAPIView(RetrieveAPIView):
    serializer_class = StockDetailSerializer
    queryset = Stock.objects.all()
    # lookup_field = 'id'


class StockCreateAPIView(CreateAPIView):
    serializer_class = StockCreateUpdateSerializer
    queryset = Stock.objects.all()


class StockUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = StockCreateUpdateSerializer
    queryset = Stock.objects.all()


class StockDestroyAPIView(DestroyAPIView):
    serializer_class = StockDetailSerializer
    queryset = Stock.objects.all()
