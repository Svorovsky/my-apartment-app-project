# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery', '0003_auto_20151105_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryservice',
            name='logo',
            field=models.ImageField(upload_to=b'Delivery/logos'),
        ),
        migrations.AlterField(
            model_name='deliveryservice',
            name='menu_file',
            field=models.FileField(upload_to=b'Delivery/menu_files'),
        ),
    ]
