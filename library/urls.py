"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from authentication.views import UserViewSet
from author.views import AuthorListCreateView, AuthorListDetailView, AuthorAPIDestroyView
from order.views import OrderViewSet, UserOrderView
from book.views import BookAPIView
from .views import base_page, HomeLists

router_user = DefaultRouter()  # можна створити один 'router' для всіх і B нього робити регістр всіх
router_user.register(r'api/v1/user', UserViewSet)
router_order = DefaultRouter()
router_order.register('order', OrderViewSet)

router_order.register(r'api/v1/user/(?P<user_id>\d+)/order/(?P<order_id>\d+)', UserOrderView, basename='order_plus_user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_page, name='home'),
    path('author/', include('author.urls')),
    path('book/', include('book.urls')),
    path('order/', include('order.urls')),
    path('user/', include('authentication.urls')),
    path('library_main/', HomeLists.as_view(), name='list_books_main'),

    # REST Framework here:
    # path('api/v1/',include(router_user.urls)),
    path('api/v1/',include(router_order.urls)), # http://127.0.0.1:8000/api/v1/order/
    path('api/v1/book/', BookAPIView.as_view()), # http://127.0.0.1:8000/api/v1/book/
    path('api/v1/book/<int:id>/', BookAPIView.as_view()), # http://127.0.0.1:8000/api/v1/book/{id}
    path('api/v1/author/', AuthorListCreateView.as_view()),
    path('api/v1/author/<int:pk>/', AuthorListDetailView.as_view()),
    path('api/v1/authordelete/<int:pk>/', AuthorAPIDestroyView.as_view()),

]

urlpatterns += router_user.urls