from django.shortcuts import render, redirect
from django.views.generic import ListView

from authentication.models import *
from book.models import Book


def base_page(request):
    # active_user = CustomUser.objects.filter(is_active = True).first()
    # print('active', active_user)
    return render(request, 'home.html')#, {'us_active' : active_user})

class HomeLists(ListView):
    """Список всіх книг """
    model = Book
    template_name = 'main_list_books.html'

    # context_object_name = 'books'    object_list -default
    # фільтр для показу книг
    def get_queryset(self):
        return Book.get_all() # .filter( ...)