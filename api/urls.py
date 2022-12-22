from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet
from .views import AuthorListCreateView, AuthorListDetailView, AuthorAPIDestroyView
from .views import OrderViewSet, UserOrderView
from .views import BookAPIView

# from .views import *


router = DefaultRouter()  # можна створити один 'router' для всіх і B нього робити регістр всіх
router.register(r'user', UserViewSet)
router.register(r'order', OrderViewSet, basename='order-users')
# router.register(r'user/(?P<user_id>\d/order', UserOrderView)

router.register(r'v1/user/(?P<user_id>[^/.]+)/order/(?P<order_id>[^/.]+)', UserOrderView,
                basename='order_plus_user')

urlpatterns = [
    # REST Framework here:
    path('v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/order/
    path('v1/book/', BookAPIView.as_view()),  # http://127.0.0.1:8000/api/v1/book/
    path('v1/book/<int:id>/', BookAPIView.as_view()),  # http://127.0.0.1:8000/api/v1/book/{id}
    path('v1/author/', AuthorListCreateView.as_view()),
    path('v1/author/<int:pk>/', AuthorListDetailView.as_view()),
    path('v1/authordelete/<int:pk>/', AuthorAPIDestroyView.as_view()),
    # path('v1/user/', CustomUserView.as_view()),

]
