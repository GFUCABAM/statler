# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statler_api', '0002_auto_20151024_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playdao',
            name='photo',
            field=models.FilePathField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='playdao',
            name='url_title',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
