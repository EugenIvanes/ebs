from itertools import product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from apishop.models import Products,PostImage
import json

from .models import *

# Create your views here.

def store(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request,'ubsshop/Store.html',context)
def cart(request):
    order, created = Order.objects.get_or_create(complete=False)
    items = OrderItem.objects.filter(order=order)
    print(items)
    context = {'items': items, 'order': order}
    print(context)
    return render(request,'ubsshop/Cart.html',context)
def checkout(request):
    context = {}
    return render(request,'ubsshop/Checkout.html',context)
def view(request, pk):
    post = get_object_or_404(Products, id=pk)
    product = Products.objects.filter(id=pk)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'ubsshop/View.html', {
        'post':post,
        'product':product,
        'photos':photos
    })
def updateItem(request):
    data = json.loads(request.body.decode('utf-8'))
    productId = data['productId']
    action = data['action']
    print('productId',productId)
    print('Action',action)
    return JsonResponse('Item was addes',safe=False)
