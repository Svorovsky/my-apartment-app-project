# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('GuestPass', '0002_auto_20151102_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=50)),
                ('service_company_name', models.CharField(max_length=50)),
                ('help_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('person', models.ForeignKey(to='GuestPass.Person')),
            ],
        ),
    ]
