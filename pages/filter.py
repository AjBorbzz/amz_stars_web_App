import django_filters
from amz_brands.models import Brand


class BrandFilter(django_filters.FilterSet):
    class Meta:
        model = Brand
        fields = ['marketplace', ]
