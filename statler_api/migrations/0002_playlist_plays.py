# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statler_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='plays',
            field=models.ManyToManyField(to='statler_api.Play', through='statler_api.PlayListEntry'),
        ),
    ]
