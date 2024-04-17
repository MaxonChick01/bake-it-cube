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


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    CHOICES = (
        ('Доставка', 'Доставка'),
        ('Самовывоз', 'Самовывоз')
    )

    customer_name = models.CharField(max_length=255, verbose_name='Имя', blank=False, null=False)
    phone = models.CharField(max_length=255, verbose_name='Телефон', blank=False, null=False)
    delivery = models.CharField(max_length=255, choices=CHOICES, verbose_name='Доставка/Самовывоз', blank=False,
                                null=False)
    address = models.CharField(max_length=255, verbose_name='Адрес', blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True, default=1, verbose_name='Этаж')
    intercom = models.CharField(max_length=255, verbose_name='Домофон', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')

    def __str__(self):
        return f'Заказ {self.customer_name} от {self.created_at.date()}'


class OrderProduct(models.Model):
    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'Количество товара'

    product = models.ForeignKey(Product, verbose_name="Продукт", blank=False, null=False, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name='Кол-во', blank=False, null=False, default=1)
    order = models.ForeignKey(Order, verbose_name='Заказ', blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        # return f'{self.product.name} - {self.count}шт.'
        return ''
