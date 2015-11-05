# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery', '0002_auto_20151104_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryservice',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='deliveryservice',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
