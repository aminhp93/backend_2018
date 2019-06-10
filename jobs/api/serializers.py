from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField
)

from jobs.models import Job

job_detail_url = HyperlinkedIdentityField(
    view_name='jobs-api:detail'
)


class JobListSerializer(ModelSerializer):
    url = job_detail_url

    class Meta:
        model = Job
        fields = [
            'id',
            'url',
            'content'
        ]


class JobDetailSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'id',
            'content'
        ]


class JobCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'content'
        ]
