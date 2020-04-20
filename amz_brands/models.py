from django.db import models


class Brand(models.Model):

    class Meta:
        ordering = ['order']

    US = 'US'
    UK = 'UK'
    CA = 'CA'
    MX = 'MX'
    MARKETPLACE = [(US, 'US'), (UK, 'UK'), (CA, 'CA'), (MX, 'MX')]
    brand_name = models.CharField(max_length=200)
    market_place = models.CharField(max_length=50, choices=MARKETPLACE)
    brand_manager = models.CharField(max_length=200)
    brand_associate = models.CharField(max_length=200)
    account_manager = models.CharField(max_length=200)
    shopify_website_uname = models.CharField(max_length=200)
    shopify_website_password = models.CharField(max_length=200)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.brand_name
