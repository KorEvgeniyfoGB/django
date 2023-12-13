from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import timedelta
from django.utils import timezone
from .models import Order, Product
from .forms import AddProductForm


def get_client_orders(request, client_id):
    today = timezone.now()
    orders_last_week = Order.objects.filter(
        client=client_id,
        date_ordered__gte=today - timedelta(days=7)).distinct()

    orders_last_month = Order.objects.filter(
        client=client_id,
        date_ordered__gte=today - timedelta(days=30)).distinct()

    orders_last_year = Order.objects.filter(
        client=client_id,
        date_ordered__gte=today - timedelta(days=365)).distinct()

    context = {
        'orders_last_week': orders_last_week,
        'orders_last_month': orders_last_month,
        'orders_last_year': orders_last_year
    }
    return render(request, 'hm2app/client_orders.html', context)


def getproduct(request):
    product = Product.objects.all()

    data = {
        'title': 'Товары',
        'product': product,
    }
    return render(request, 'hm2app/product.html', data)


def addproduct(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = AddProductForm()
    data = {
        'title': 'Добавление товара',
        'form': form
    }
    return render(request, 'hm2app/addproduct.html', data)