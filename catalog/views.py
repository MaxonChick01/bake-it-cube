from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    data['floor'] = int(data['floor']) if data['floor'] else None
    order = Order.objects.create(**data)
    order_product = eval(request.POST.get('products'))
    for product, count in order_product.items():
        OrderProduct.objects.create(order=order, product=Product.objects.get(id=product), count=count)

    return HttpResponse({}, status=200)


@csrf_exempt
def cart(request):
    if request.method == "POST":
        cart_request = eval(request.POST['cart'])
        cart_response = {}
        for id, count in cart_request.items():
            product = Product.objects.get(pk=int(id))
            cart_response[id] = {
                'count': count,
                'name': product.name,
                'weight': product.weight,
                'price': product.price,
                'photo_url': product.image.url
            }
        return JsonResponse(cart_response)