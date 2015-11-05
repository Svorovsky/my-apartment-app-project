# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_auto_20151105_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='image',
            field=models.ImageField(upload_to=b'News/images'),
        ),
    ]
