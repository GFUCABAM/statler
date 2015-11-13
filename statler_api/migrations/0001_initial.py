# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import statler_api.models.statler_model


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('url_title', models.CharField(max_length=32, unique=True)),
                ('title', models.CharField(max_length=256)),
                ('director', models.CharField(max_length=256)),
                ('actors', models.CharField(max_length=256, blank=True)),
                ('description', models.CharField(max_length=1024, blank=True)),
                ('image', models.FileField(upload_to='static', blank=True, null=True)),
                ('show_times', models.CharField(max_length=256, blank=True)),
            ],
            bases=(models.Model, statler_api.models.statler_model.StatlerModel),
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('url_title', models.CharField(max_length=32)),
            ],
            bases=(models.Model, statler_api.models.statler_model.StatlerModel),
        ),
        migrations.CreateModel(
            name='PlayListEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('play_list_order', models.IntegerField(null=True, blank=True)),
                ('play', models.ForeignKey(to='statler_api.Play')),
                ('play_list', models.ForeignKey(to='statler_api.PlayList')),
            ],
            bases=(models.Model, statler_api.models.statler_model.StatlerModel),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('rating', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('play', models.ForeignKey(to='statler_api.Play')),
            ],
            bases=(models.Model, statler_api.models.statler_model.StatlerModel),
        ),
    ]
