from django.shortcuts import render, redirect
from authentication.models import *

def base_page(request):
    active_user = CustomUser.objects.filter(is_active = True).first()
    print('active', active_user)
    return render(request, 'home.html', {'us_active' : active_user})
