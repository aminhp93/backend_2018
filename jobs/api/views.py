from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView
)
from jobs.models import Job

from .serializers import (
    JobListSerializer,
    JobDetailSerializer,
    JobCreateUpdateSerializer
)


class JobListAPIView(ListAPIView):
    serializer_class = JobListSerializer
    queryset = Job.objects.all()


class JobDetailAPIView(RetrieveAPIView):
    serializer_class = JobDetailSerializer
    queryset = Job.objects.all()
    # lookup_field = 'id'


class JobCreateAPIView(CreateAPIView):
    serializer_class = JobCreateUpdateSerializer
    queryset = Job.objects.all()


class JobUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = JobCreateUpdateSerializer
    queryset = Job.objects.all()


class JobDestroyAPIView(DestroyAPIView):
    serializer_class = JobDetailSerializer
    queryset = Job.objects.all()
