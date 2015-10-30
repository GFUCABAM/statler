# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statler_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayDAO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('url_title', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=256)),
                ('director', models.CharField(max_length=256)),
                ('actors', models.CharField(blank=True, max_length=256)),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('photo', models.FilePathField(blank=True)),
                ('show_times', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='PlayListDAO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('url_title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PlayListEntryDAO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('play_list_order', models.IntegerField(null=True, blank=True)),
                ('play', models.ForeignKey(to='statler_api.PlayDAO')),
                ('play_list', models.ForeignKey(to='statler_api.PlayListDAO')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewDAO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('text', models.TextField()),
                ('rating', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('play', models.ForeignKey(to='statler_api.PlayDAO')),
            ],
        ),
        migrations.DeleteModel(
            name='Play',
        ),
    ]
