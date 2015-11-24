# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GMP', '0003_auto_20151124_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lista',
            field=models.OneToOneField(related_name='lista', null=True, default=None, blank=True, to='GMP.PlayList'),
        ),
    ]
