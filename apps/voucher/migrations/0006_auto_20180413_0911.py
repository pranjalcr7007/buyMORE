# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-13 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0005_auto_20180402_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucherset',
            name='count',
            field=models.PositiveIntegerField(verbose_name='Number of vouchers'),
        ),
    ]
