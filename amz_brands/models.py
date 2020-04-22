from django.db import models


class Brand(models.Model):

    class Meta:
        ordering = ['order']

    brand_name = models.CharField(max_length=200)
    marketplace = models.CharField(max_length=50)
    brand_manager = models.CharField(max_length=200)
    brand_associate = models.CharField(max_length=200)
    account_manager = models.CharField(max_length=200)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.brand_name
