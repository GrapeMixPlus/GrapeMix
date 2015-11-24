# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GMP', '0005_auto_20151124_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='song',
            name='tittle',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
    ]
