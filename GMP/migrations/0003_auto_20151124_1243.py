# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GMP', '0002_auto_20151124_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lista',
            field=models.OneToOneField(related_name='lista', default=None, blank=True, to='GMP.PlayList'),
        ),
    ]
