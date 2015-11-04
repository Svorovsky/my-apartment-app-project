# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('first_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('apartment_number', models.CharField(max_length=5)),
                ('car_id', models.CharField(max_length=12)),
            ],
        ),
    ]
