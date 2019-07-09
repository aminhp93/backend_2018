from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)


class TinderLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 10


class TinderPageNumberPagination(PageNumberPagination):
    page_size = 1000
