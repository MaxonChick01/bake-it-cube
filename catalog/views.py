from django.shortcuts import render, HttpResponse
from .models import Category, Product, Info, OrderProduct, Order


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


def order(request):
    data = {
        'customer_name': request.POST.get('name'),
        'phone': request.POST.get('phone'),
        'delivery': request.POST.get('delivery'),
        'address': request.POST.get('address', None),
        'floor': request.POST.get('floor', None),
        'intercom': request.POST.get('flat', None)
    }
    if data['delivery'] == 'true':
        data['delivery'] = 'Доставка'
    else:
        data['delivery'] = 'Самовывоз'

    data['floor'] = int(data['floor'])
    order = Order.objects.create(**data)


    return HttpResponse({}, status=200)
