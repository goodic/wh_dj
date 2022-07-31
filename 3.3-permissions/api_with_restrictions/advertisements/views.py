from django_filters import rest_framework as filters, DateFromToRangeFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class CreatedAtFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at']


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = CreatedAtFilter
    filterset_fields = ['status']
    permission_classes = [IsOwnerOrReadOnly]

