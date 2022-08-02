from django_filters import rest_framework as filters, DateFromToRangeFilter, CharFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter()
    status = CharFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']

