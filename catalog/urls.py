from django.urls import path
from .views import main, order, cart

urlpatterns = [
    path('', main),
    path('api/order', order),
    path('api/cart', cart),
]