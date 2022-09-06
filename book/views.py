from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView

from .models import Book
from .forms import BookForm

def list_books(request):
    return render(request, 'book/book_list.html', { 'books' : Book.get_all()})

class AddBook(CreateView):
    form_class = BookForm
    template_name = 'book/add_book.html'


# def add_book(request):

def detail_book(request,id):
    content = {
        'dict_b': Book.get_by_id(id).to_dict(),
        'book_obj' :  Book.get_by_id(id)
    }
    return render(request, 'book/book_detail.html', {'book':  content})

def change_book(request, id=0):
    try:
        if request.method == 'GET':
            if id ==0:
                form = BookForm()
            else:
                book = Book.get_by_id(id)
                form = BookForm(request.POST or None, instance=book)
                # form = AddAuthorForm(initial=dict(field_name=get_form_kwargs)
            return render(request, 'book/edit_book.html', {'form': form})
        else:
        # elif request.method == 'POST':
            if id==0:
                form = BookForm(request.POST)
            else:
                book = Book.get_by_id(id)
                form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                messages.success(request, f'Changed book: {book.name} success !')
            else:
                return render(request, 'book/edit_book.html', {'form': form})
            return redirect('list_books')
    except Exception:
        messages.error(request, f'You catch error!')
# @login_required
# def edit_book(request, id=None, template_name='book/edit_book.html'):
#     if id:
#         # book = Book.get_by_id(id)
#         book = get_object_or_404(Book, pk=id)
#         # if article.author != request.user:
#         #     return HttpResponseForbidden()
#     else:
#         book = Book(author=request.user)
#
#     form = BookForm(request.POST or None, instance=book)
#     if request.POST and form.is_valid():
#         form.save()

        # Save was successful, so redirect to another page
        # redirect_url = reverse(article_save_success)
    #     return redirect('list_book')
    #
    # return render(request, template_name, {'form': form})
@login_required(login_url='login_url')
def delete_book(request, id):
    try:
        var_book_name = Book.get_by_id(id).name
        Book.delete_by_id(id)
        messages.info(request, f'You have delete book {var_book_name}. Success !')
        return redirect('list_books')
    except Exception:
        messages.warning(request, 'Something wrong')
        return redirect('list_books')
