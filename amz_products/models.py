from django.db import models
from amz_brands.models import Brand
from datetime import datetime


class Product(models.Model):
    stat_active = 'Active'
    stat_inactive = 'Inactive'
    PRODUCT_STATUS = [(stat_active, 'Active'), (stat_inactive, 'Inactive')]
    prod_brand = models.OneToOneField(
        Brand, on_delete=models.CASCADE, default=None)
    prod_marketplace = models.CharField(max_length=5)
    prod_status = models.CharField(max_length=20, choices=PRODUCT_STATUS)
    prod_SKU = models.CharField(max_length=20)
    prod_Parent_ASIN = models.CharField(max_length=20)
    prod_Child_ASIN = models.CharField(max_length=50)
    prod_title = models.CharField(max_length=100)
    prod_num_of_reviews = models.IntegerField()
    prod_star_rating = models.FloatField()
    date_updated = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.prod_title[:6]
