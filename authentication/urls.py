from django.urls import include, path
from .views import *

urlpatterns = [
    path('', list_users, name='list_users'),
    path('registration/', register, name='register_url'),
    path('login/', user_login, name='login_url'),
    path('login_django/', login_django, name='login_django'),
    path('logout/', user_logout, name='logout_url'),
    path('delete/<int:id>/', delete_user, name='user_delete_url'),
    path('edit/<int:user_id>/', edit_user, name='user_edit_url'),
    path('user_detail/<int:id>/', detail_user, name='user_detail_url'),

]
