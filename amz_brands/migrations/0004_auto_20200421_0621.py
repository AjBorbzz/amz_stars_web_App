# Generated by Django 3.0.5 on 2020-04-21 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amz_brands', '0003_auto_20200421_0556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='market_place',
            new_name='marketplace',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='shopify_website_password',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='shopify_website_uname',
        ),
    ]
