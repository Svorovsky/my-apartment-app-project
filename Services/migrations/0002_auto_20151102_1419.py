# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='arrear',
            field=models.CommaSeparatedIntegerField(default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='monthly_bill',
            field=models.CommaSeparatedIntegerField(default=0.0, max_length=12),
            preserve_default=False,
        ),
    ]
