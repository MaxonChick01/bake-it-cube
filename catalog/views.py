from django.shortcuts import render
from .models import Category, Product


def main(request):
    category = request.GET.get('category', '0')
    if category == '0':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category=category)

    context = {}
    categories = Category.objects.all()
    context['label'] = "YourMeal"
    context['categories'] = categories
    context['products'] = products
    return render(request, 'index.html', context)
