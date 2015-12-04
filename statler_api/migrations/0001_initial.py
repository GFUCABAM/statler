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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('url_title', models.CharField(unique=True, max_length=32)),
                ('title', models.CharField(max_length=256)),
                ('director', models.CharField(max_length=256)),
                ('actors', models.CharField(blank=True, max_length=256)),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('image', models.FileField(upload_to='static', blank=True, null=True)),
                ('show_times', models.CharField(blank=True, max_length=256)),
            ],
            bases=(models.Model, statler_api.models.statler_model.StatlerModel),
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('url_title', models.CharField(max_length=32)),
            ],
            bases=(models.Model, statler_api.models.statler_model.StatlerModel),
        ),
        migrations.CreateModel(
            name='PlayListEntry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('play_list_order', models.IntegerField(blank=True, null=True)),
                ('play', models.ForeignKey(to='statler_api.Play')),
                ('play_list', models.ForeignKey(to='statler_api.PlayList')),
            ],
            bases=(models.Model, statler_api.models.statler_model.StatlerModel),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('text', models.TextField()),
                ('rating', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('play', models.ForeignKey(to='statler_api.Play')),
            ],
            bases=(models.Model, statler_api.models.statler_model.StatlerModel),
        ),
        migrations.AddField(
            model_name='playlist',
            name='plays',
            field=models.ManyToManyField(to='statler_api.Play', through='statler_api.PlayListEntry'),
        ),
    ]
