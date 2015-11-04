# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to=b' ')),
                ('menu_file', models.FileField(upload_to=b' ')),
            ],
        ),
    ]
