from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_list_or_404
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from authentication.models import CustomUser
from book.models import Book
from .forms import OrderForm
from .models import Order

def list_orders(request):
    data = Order.get_all()
    return render(request, 'order/order_list.html', {'orders':data})

def my_orders(request):
    try:
        current_user  = request.user
        messages.info(request, f"All orders for user name: '{current_user}', email: {current_user.email} ")
        data = Order.objects.filter(user_id = current_user.id)
        print(data)
    except:
        messages.warning(request, f'Something went wrong. Orders for: {current_user}')
        return redirect('home')

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
        # print(form.data)<QueryDict: {'csrfmiddlewaretoken': ['trJ'], 'book': ['1'], 'plated_end_at': ['2022-09-13']}>
        if form.is_valid():
            book = request.POST.get('book')
            plated_end_at = request.POST.get('plated_end_at')
            user = request.user.id
            print(user, book, plated_end_at)
            new_ord = Order(user=CustomUser.get_by_id(user), book=Book.get_by_id(book), plated_end_at=plated_end_at)
            new_ord.save()
            print('new ORDER here :', new_ord, book, user)
            messages.success(request, f'book:{book}. new order was created')
        #   'plated_end_at': forms.DateInput(attrs={'type': 'date', 'min': date_today, 'max': end_date}),
        #   end_date = datetime.date.today() + datetime.timedelta(days=14)
        #   timezone.now() + datetime.timedelta(days=14)
        #   print('USER ID', user, 'book id', book_id)
            return redirect('list_orders')
    else:
        form = OrderForm()
    return render(request, 'order/new_order.html', {'form': form})

