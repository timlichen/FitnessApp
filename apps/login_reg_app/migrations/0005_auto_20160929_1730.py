# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0004_auto_20160929_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='goal',
            field=models.IntegerField(),
        ),
    ]
