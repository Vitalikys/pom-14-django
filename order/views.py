from django.shortcuts import render


def list_orders(request):
    return render(request, 'order/order_list.html')
