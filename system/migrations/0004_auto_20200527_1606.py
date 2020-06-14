# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-05-27 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20190506_0139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagefile',
            options={'verbose_name': 'image table', 'verbose_name_plural': 'image table'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-reorder'], 'verbose_name': 'news and notification', 'verbose_name_plural': 'news and notification'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['-reorder'], 'verbose_name': 'slider', 'verbose_name_plural': 'slider'},
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(verbose_name='contents'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='news',
            name='types',
            field=models.SmallIntegerField(choices=[(11, 'news'), (12, 'notification')], default=11, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create time'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='end_time'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='img',
            field=models.ImageField(upload_to='slider', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='delete or not'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='name',
            field=models.CharField(max_length=32, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='reorder',
            field=models.SmallIntegerField(default=0, help_text='The higher the number, the higher the front', verbose_name='reorder'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start_time'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='target_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='target url'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='types',
            field=models.SmallIntegerField(choices=[(11, 'home page')], default=11, verbose_name='position'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='update time'),
        ),
    ]
