# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_auto_20151102_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='person',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
