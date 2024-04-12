from django.contrib import admin
from .models import Product, Ingredient, Category, Info
from solo.admin import SingletonModelAdmin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'price', 'weight')
    filter_horizontal = ('ingredients',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category


admin.site.register(Info, SingletonModelAdmin)
