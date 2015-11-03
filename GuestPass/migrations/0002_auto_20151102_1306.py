# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('GuestPass', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guestpass',
            options={'verbose_name_plural': 'Guest passes'},
        ),
        migrations.AddField(
            model_name='person',
            name='car_id',
            field=models.CharField(default=datetime.datetime(2015, 11, 2, 13, 6, 48, 46990, tzinfo=utc), max_length=12),
            preserve_default=False,
        ),
    ]
