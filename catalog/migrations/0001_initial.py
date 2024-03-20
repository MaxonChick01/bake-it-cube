# Generated by Django 5.0.3 on 2024-03-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.PositiveIntegerField(verbose_name='Цена в рублях')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Описание')),
                ('weight', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Вес')),
                ('kkal', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Ккал')),
                ('ingredients', models.ManyToManyField(to='catalog.ingredients', verbose_name='Состав')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]