# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBills', '0002_auto_20151104_1555'),
        ('GuestPass', '0002_auto_20151102_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestpass',
            name='person',
            field=models.ForeignKey(to='UserProfile.Person'),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
