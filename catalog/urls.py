from django.urls import path
from .views import main, order

urlpatterns = [
    path('', main),
    path('api/order', order)
]