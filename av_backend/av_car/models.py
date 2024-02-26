## -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Car(models.Model):
    category = models.ForeignKey(Category, related_name='av_car', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    price = models.CharField(max_length=50)
    price_usd = models.CharField(max_length=50)
    image = models.TextField(max_length=1000)
    parameter = models.TextField(max_length=500)
    description = models.TextField(max_length=500)
    modification = models.TextField(max_length=500)
    all_modification = models.TextField(max_length=500)
    location = models.TextField(max_length=500)
    comment = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'name'),)

    def __str__(self):
        return self.name
