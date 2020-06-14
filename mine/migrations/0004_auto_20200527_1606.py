# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-05-27 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0003_auto_20200526_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.SmallIntegerField(choices=[(10, 'shopping cart'), (11, 'submitted'), (12, 'paid'), (13, 'shipped'), (14, 'finished'), (15, 'deleted')], default=10, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(10, 'shopping cart'), (11, 'submitted'), (12, 'paid'), (13, 'shipped'), (14, 'finished'), (15, 'deleted')], default=11, verbose_name='订单状态'),
        ),
    ]