# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestPass', '0003_auto_20151104_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestpass',
            name='car_id',
        ),
        migrations.AddField(
            model_name='guest',
            name='car_id',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
