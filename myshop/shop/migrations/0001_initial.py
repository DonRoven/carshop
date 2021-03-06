# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='\u0417\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u0442\u043e\u0432\u0430\u0440\u0443')),
                ('description', models.TextField(blank=True, verbose_name='\u041e\u043f\u0438\u0441')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u0426\u0456\u043d\u0430')),
                ('stock', models.PositiveIntegerField(verbose_name='\u041d\u0430 \u0441\u043a\u043b\u0430\u0434\u0456')),
                ('available', models.BooleanField(default=True, verbose_name='\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u0438\u0439')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
