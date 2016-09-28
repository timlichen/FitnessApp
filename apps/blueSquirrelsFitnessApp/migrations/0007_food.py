# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg_app', '0003_auto_20160928_1730'),
        ('blueSquirrelsFitnessApp', '0006_auto_20160928_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=255)),
                ('calories', models.DecimalField(decimal_places=2, max_digits=7)),
                ('carbohydrates', models.DecimalField(decimal_places=2, max_digits=7)),
                ('lipids', models.DecimalField(decimal_places=2, max_digits=7)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=7)),
                ('sugar', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_reg_app.User')),
            ],
        ),
    ]
