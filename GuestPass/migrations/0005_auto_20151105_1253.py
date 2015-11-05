# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestPass', '0004_auto_20151104_2322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guestpass',
            options={'verbose_name_plural': 'GuestPasses'},
        ),
    ]
