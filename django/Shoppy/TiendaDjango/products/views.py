from django.shortcuts import render
from .models import Product


def hola_mundo(request):
    products = Product.objects.order_by('id')
    return render(request, 'index.html', {'productos': products})
