from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import OrderForm
from .models import Order


def list_orders(request):
    data = Order.get_all()
    return render(request, 'order/order_list.html', {'orders':data})

def my_orders(request):
    current_user  = request.user
    messages.info(request, f"Info about all orders for user: '{current_user}' ")
    data = Order.objects.filter(user_id= current_user.id).values()
    return render(request, 'order/all_my_orders.html', {'orders':data})

@login_required(login_url='login_url')
def delete_order(request, order_id):
    Order.delete_by_id(order_id)
    messages.success(request, 'You have delete order. Success !')
    return redirect('list_orders')

@login_required(login_url='login_url')
def edit_order(request, order_id=None):
    if order_id:
        order = Order.get_by_id(order_id)
    form = OrderForm(request.POST or None, instance=order)
    if request.POST and form.is_valid():
        form.save()
        # Save was successful, so redirect to another page
        messages.success(request, f'Changes order: {order.id} success !')
        return redirect('list_orders')
    context = {'form': form, 'order': order}
    return render(request, 'order/edit_order.html', context=context)

@login_required(login_url='login_url')
def add_order(request):
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'book: new order:  ok')
            return redirect('list_orders')
    else:
        form = OrderForm()
    return render(request, 'order/new_order.html', {'form': form})
