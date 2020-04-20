import django_filters
from .models import Brand


class BrandFilter(django_filters.FilterSet):
    class Meta:
        model = Brand
        fields = ['market_place', ]
