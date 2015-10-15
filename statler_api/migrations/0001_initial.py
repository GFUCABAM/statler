# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('url_title', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
            ],
        ),
    ]
