from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField
)

from stocks.models import Stock

stock_detail_url = HyperlinkedIdentityField(
    view_name='stocks-api:detail'
)

class StockListSerializer(ModelSerializer):
    url = stock_detail_url
    class Meta:
        model = Stock
        fields = [
            'id',
            'url',
            'Symbol'
        ]

class StockDetailSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            'id',
            'Symbol',
            'Close',
            'Volume'
        ]
    
class StockCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            'Symbol'
        ]