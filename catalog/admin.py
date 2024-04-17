from django.contrib import admin
from .models import Product, Ingredient, Category, Info, Order, OrderProduct
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


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInline, ]
    fields = ('customer_name', 'phone', 'delivery', 'address', 'floor', 'intercom', 'created_at')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Info, SingletonModelAdmin)
