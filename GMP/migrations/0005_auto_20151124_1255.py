# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GMP', '0004_auto_20151124_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='lista',
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(related_name='ownerplaylist', default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
