# Generated by Django 3.0.5 on 2020-05-01 04:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amz_sfr_tracker', '0002_auto_20200501_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackremoval',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='feedbackremoval',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
