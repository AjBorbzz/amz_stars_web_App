from django.forms import ModelForm
from .models import Brand


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name', 'marketplace', 'brand_manager',
                  'brand_associate', 'account_manager']
