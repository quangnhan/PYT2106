from django.db import models
from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def product_list(request):
    product_list = []
    
    for product in Product.objects.all():
        product_list.append({
            'name' : product.name,
            'price' : product.price,
        })

    return JsonResponse({'product_list' : product_list})
