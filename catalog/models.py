from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    name = models.CharField(max_length=255, verbose_name='Название', blank=False, null=False)
    price = models.PositiveIntegerField(verbose_name='Цена в рублях', blank=False, null=False)
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='')
    weight = models.PositiveIntegerField(verbose_name='Вес', blank=True, null=True, default=0)
    kkal = models.PositiveIntegerField(verbose_name='Ккал', blank=True, null=True, default=0)
    ingredients = models.ManyToManyField('Ingredients', verbose_name='Состав')

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    name = models.CharField(max_length=255, verbose_name='Название', blank=False, null=False)