from django.shortcuts import render

def catalog(request):
    return render(request, 'shop/catalog.html')

def orders(request):
    return render(request, 'shop/order.html')

def order_create(request):
    return render(request, 'shop/order_create.html')
