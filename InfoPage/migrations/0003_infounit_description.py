# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoPage', '0002_auto_20151104_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='infounit',
            name='description',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
