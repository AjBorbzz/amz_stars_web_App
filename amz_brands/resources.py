from import_export import resources
from .models import Brand


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand
