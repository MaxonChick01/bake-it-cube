from django.shortcuts import render
from .models import Category, Product, Info


def main(request):
    context = {}
    category = request.GET.get('category', '0')
    if category == '0':
        products = Product.objects.all()
        context['selected_category'] = "Все"
    else:
        products = Product.objects.filter(category=category)
        context['selected_category'] = Category.objects.get(id=category).name

    categories = Category.objects.all()
    context['contacts'] = Info.objects.get()
    context['label'] = "YourMeal"
    context['categories'] = categories
    context['products'] = products
    return render(request, 'index.html', context)
