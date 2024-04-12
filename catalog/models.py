from django.db import models
from solo.models import SingletonModel


class Info(SingletonModel):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    phone = models.CharField(max_length=255, verbose_name='Телефон', blank=False, null=False)
    vk = models.CharField(max_length=255, verbose_name='ВК', blank=False, null=False)
    tg = models.CharField(max_length=255, verbose_name='Телеграм', blank=False, null=False)

    def __str__(self):
        return "Контакты для связи"



class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    name = models.CharField(max_length=255, verbose_name='Название', blank=False, null=False)
    price = models.PositiveIntegerField(verbose_name='Цена в рублях', blank=False, null=False)
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='')
    weight = models.PositiveIntegerField(verbose_name='Вес', blank=True, null=True, default=0)
    kkal = models.PositiveIntegerField(verbose_name='Ккал', blank=True, null=True, default=0)
    ingredients = models.ManyToManyField('Ingredient', verbose_name='Состав')
    image = models.ImageField(verbose_name='Изображение', upload_to='photos', default='')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    name = models.CharField(max_length=255, verbose_name='Название', blank=False, null=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=255, verbose_name='Название', blank=False, null=False)
    image = models.ImageField(verbose_name='Изображение', upload_to='categories', default='')

    def __str__(self):
        return self.name

