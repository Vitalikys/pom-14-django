from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from authentication.models import CustomUser
from book.models import Book
from .forms import OrderForm
from .models import Order

from rest_framework import viewsets, status

from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# class OrderViewSet(viewsets.ViewSet):
#     def list(self, request):
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk =None):
#         queryset = Order.objects.all()
#         order = get_object_or_404(queryset, pk= pk)
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)



def list_orders(request):
    data = Order.get_all()
    return render(request, 'order/order_list.html', {'orders':data})

def my_orders(request):
    current_user  = request.user
    messages.info(request, f"All orders for user name: '{current_user}', email: {current_user.email} ")
    data = Order.objects.filter(user_id = current_user.id)
    print(data)
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
            import datetime
            form.save()
            # print(form.cleaned_data)
            # book_id = int(form.cleaned_data['book'].id)
            # book = Book.get_by_id(book_id)
            # # user = CustomUser.get_by_id(request.user.id)
            # user = request.user.id
            # # timezone.now() + datetime.timedelta(days=14)
            # from django.utils import timezone
            # date = timezone.now() + datetime.timedelta(days=14)
            # print(book, book_id, user, date)
            # Order.create(user=user, book= book, plated_end_at=date)
            # messages.success(request, f'book: new order:  ok')
            return redirect('list_orders')
    else:
        form = OrderForm()
    return render(request, 'order/new_order.html', {'form': form})
