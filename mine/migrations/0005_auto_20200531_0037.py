# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-05-30 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0004_auto_20200527_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'shopping cart', 'verbose_name_plural': 'shopping cart'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'product rating', 'verbose_name_plural': 'product rating'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'order management', 'verbose_name_plural': 'order management'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='amount',
            field=models.FloatField(verbose_name='total price'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='count',
            field=models.PositiveIntegerField(verbose_name='Purchase quantity'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create time'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Main image of the product'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='name',
            field=models.CharField(max_length=128, verbose_name='product name'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='mine.Order', verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='origin_price',
            field=models.FloatField(verbose_name='Original price'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.IntegerField(verbose_name='Exchange price'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.SmallIntegerField(choices=[(10, 'shopping cart'), (11, 'submitted'), (12, 'paid'), (13, 'shipped'), (14, 'finished'), (15, 'deleted')], default=10, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='update time'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create time'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='desc',
            field=models.CharField(max_length=256, verbose_name='comment content'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='is_anonymous',
            field=models.BooleanField(default=True, verbose_name='Is it anonymous'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='valid or not'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='reorder',
            field=models.SmallIntegerField(default=0, verbose_name='reorder'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='score',
            field=models.FloatField(default=10.0, verbose_name='Product Rating'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='score_deliver',
            field=models.FloatField(default=10.0, verbose_name='Distribution service scores'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='score_package',
            field=models.FloatField(default=10.0, verbose_name='Express packaging scores'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='score_speed',
            field=models.FloatField(default=10.0, verbose_name='Delivery speed scores'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='update time'),
        ),
        migrations.AlterField(
            model_name='order',
            name='buy_amount',
            field=models.FloatField(verbose_name='Total price'),
        ),
        migrations.AlterField(
            model_name='order',
            name='buy_count',
            field=models.IntegerField(default=1, verbose_name='Purchase quantity'),
        ),
        migrations.AlterField(
            model_name='order',
            name='express_no',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='delivery ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='express_type',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='express delivery'),
        ),
        migrations.AlterField(
            model_name='order',
            name='remark',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='remark'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sn',
            field=models.CharField(max_length=32, verbose_name='Order number'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(10, 'shopping cart'), (11, 'submitted'), (12, 'paid'), (13, 'shipped'), (14, 'finished'), (15, 'deleted')], default=11, verbose_name='Order Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_address',
            field=models.CharField(max_length=256, verbose_name='detail address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_area',
            field=models.CharField(max_length=32, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_phone',
            field=models.CharField(max_length=32, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_user',
            field=models.CharField(max_length=32, verbose_name='Receiver'),
        ),
    ]