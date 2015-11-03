# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statler_api', '0003_auto_20151101_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playdao',
            name='photo',
        ),
        migrations.AddField(
            model_name='playdao',
            name='image',
            field=models.FileField(null=True, blank=True, upload_to='TODO'),
        ),
    ]
