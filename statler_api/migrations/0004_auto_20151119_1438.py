# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statler_api', '0003_auto_20151112_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='playlist',
            name='is_dynamically_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='playlist',
            name='num_to_order_dynamically',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
