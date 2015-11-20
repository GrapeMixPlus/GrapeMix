# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('GMP', '0004_artist_playlist_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL), max_length=20, verbose_name='Name'),
        ),
    ]
