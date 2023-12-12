from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from .models import Order


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
