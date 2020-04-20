from django.forms import ModelForm
from .models import Brand


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name', 'market_place', 'brand_manager',
                  'brand_associate', 'account_manager', 'shopify_website_uname', 'shopify_website_password']
