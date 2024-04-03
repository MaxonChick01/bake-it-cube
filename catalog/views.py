from django.shortcuts import render
from .models import Category, Product


def main(request):
    context = {}
    categories = Category.objects.all()
    products = Product.objects.all()
    context['label'] = "YourMeal"
    context['categories'] = categories
    context['products'] = products
    return render(request, 'index.html', context)
