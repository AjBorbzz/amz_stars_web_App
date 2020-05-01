from django.db import models
from django.contrib.auth.models import User
from amz_brands.models import Brand
from amz_products.models import Product
from datetime import datetime


class FeedbackRemoval(models.Model):
    ob_lang = 'Obscene Language'
    prod_rev = 'Product Review'
    sel_inc = 'Seller PPI included'
    shi_del = 'Shipment Delays'
    rem_reason = [(ob_lang, 'Obscene Language'), (prod_rev, 'Product Review'),
                  (sel_inc, 'Seller PPI included'), (shi_del, 'Shipment Delays')]
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    brand_name = models.OneToOneField(Brand, on_delete=models.CASCADE)
    product_name = models.OneToOneField(Product, on_delete=models.CASCADE)
    case_id = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)
    reason_for_removal = models.CharField(max_length=50, choices=rem_reason)
    created_date = models.DateTimeField(default=datetime.now)
    updated_date = models.DateTimeField(default=datetime.now)
