from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('prod_title', 'date_updated')
    display_links = ('date_updated',)
    search_fields = ('PRODUCT_STATUS', 'prod_title', 'date_updated')


admin.site.register(Product, ProductAdmin)
