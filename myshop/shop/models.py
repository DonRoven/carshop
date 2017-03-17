# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse



# model category
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = u'Категорія'
        verbose_name_plural = u'Категорії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])


# Product model
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name=u"Категорія")
    name = models.CharField(max_length=200, db_index=True, verbose_name=u"Назва")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name=u"Зображення товару")
    description = models.TextField(blank=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u"Ціна")
    stock = models.PositiveIntegerField(verbose_name=u"На складі")
    available = models.BooleanField(default=True, verbose_name=u"Доступний")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = u'Назва товару'
        verbose_name_plural = u'Назви товарів'

        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])