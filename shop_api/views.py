from django.shortcuts import render
from catalog.models import Product, Ingredient, Category
from rest_framework import viewsets
from .serializers.products import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
