from django.shortcuts import render
from .models import Book

def list_books(request):
    return render(request, 'book/book_list.html', { 'books' : Book.get_all()})


def detail_book(request,id):
    content = {
        'dict_b': Book.get_by_id(id).to_dict(),
        'book_obj' :  Book.get_by_id(id)
    }
    return render(request, 'book/book_detail.html', {'book':  content})
