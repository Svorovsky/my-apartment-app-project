# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GuestPass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car_id', models.CharField(max_length=12)),
                ('date', models.DateField()),
                ('guest', models.ForeignKey(to='GuestPass.Guest')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('apartment_number', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='guestpass',
            name='person',
            field=models.ForeignKey(to='GuestPass.Person'),
        ),
    ]
