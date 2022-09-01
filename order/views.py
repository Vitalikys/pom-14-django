from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Order


def list_orders(request):
    data = Order.get_all()
    return render(request, 'order/order_list.html', {'orders':data})

@login_required(login_url='login_url')
def delete_order(request, order_id):
    Order.delete_by_id(order_id)
    messages.success(request, 'You have delete order. Success !')
    return redirect('list_orders')

