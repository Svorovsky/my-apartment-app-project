# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_auto_20151102_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('service_company_name', models.CharField(max_length=50)),
                ('service_company_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
    ]
