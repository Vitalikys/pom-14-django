from django.urls import include, path
from .views import *

urlpatterns = [
    path('', list_orders, name='list_orders'),
    path('my_orders/', my_orders, name='my_orders'),
    path('delete_order/<int:order_id>', delete_order, name='order_delete_url'),
]
