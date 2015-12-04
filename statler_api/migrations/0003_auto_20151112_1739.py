# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statler_api', '0002_playlist_plays'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='top_review_rank',
            field=models.IntegerField(null=True, blank=True, default=None),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('play', 'top_review_rank')]),
        ),
    ]
