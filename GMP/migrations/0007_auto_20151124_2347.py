# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GMP', '0006_auto_20151124_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='tittle',
            new_name='titulo',
        ),
    ]
