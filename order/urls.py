from django.urls import include, path
from .views import *

urlpatterns = [
    path('', list_orders, name='list_orders'),
]
