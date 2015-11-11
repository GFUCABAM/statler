# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statler_api', '0004_auto_20151102_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopReviewDAO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('review_order', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='playdao',
            name='image',
            field=models.FileField(null=True, upload_to='static', blank=True),
        ),
        migrations.AddField(
            model_name='topreviewdao',
            name='play',
            field=models.ForeignKey(to='statler_api.PlayDAO'),
        ),
        migrations.AddField(
            model_name='topreviewdao',
            name='review',
            field=models.ForeignKey(to='statler_api.ReviewDAO'),
        ),
    ]
