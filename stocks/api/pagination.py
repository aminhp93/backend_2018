from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)


class StockLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 10


class StockPageNumberPagination(PageNumberPagination):
    page_size = 10
