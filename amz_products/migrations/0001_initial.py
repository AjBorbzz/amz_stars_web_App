# Generated by Django 3.0.5 on 2020-04-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_marketplace', models.CharField(max_length=5)),
                ('prod_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=20)),
                ('prod_SKU', models.CharField(max_length=20)),
                ('prod_Parent_ASIN', models.CharField(max_length=20)),
                ('prod_Child_ASIN', models.CharField(max_length=50)),
                ('prod_title', models.CharField(max_length=100)),
                ('prod_num_of_reviews', models.IntegerField(max_length=50)),
                ('prod_star_rating', models.FloatField()),
            ],
        ),
    ]
