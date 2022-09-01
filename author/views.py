from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Author
from .forms import AddAuthorForm

@login_required(login_url='login_url')
def list_author(request):
    return render(request, 'author/author_list.html', {'author': Author.get_all() } )

def add_author(request):
    if request.method == 'POST':
        form= AddAuthorForm(request.POST) # забираємо дані
        if form.is_valid():
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            patronymic = request.POST.get('patronymic')
            try:
                Author.create(name, surname, patronymic)
                messages.success(request, f'Add new author: {name} success !')
                return redirect('list_author')
            except Exception:
                messages.error(request, 'Error creation author... щось пішло не так')
    else:
        form = AddAuthorForm() #створ екземпл пустої форми
    return render(request, 'author/add_author.html', {'form':form} )



'''
# def add_author(request):
#     if request.method == 'POST':
#         form= AddAuthorForm(request.POST) # забираємо дані
#         if form.is_valid():
#             form.save()
#             return redirect('list_author')
#     else:
#         form = AddAuthorForm() #створ екземпл пустої форми
#     return render(request, 'author/add_author.html', {'form':form} )

'''
@login_required(login_url='login_url')
def delete_author(request, id):
    Author.delete_by_id(id)
    messages.success(request, 'You have delete author. Success !')
    return redirect('list_author')

# class CreateAuthor(CreateView):
#     form_class = AddAuthorForm
#     template_name = 'author/add_author.html'
    # login_url = 'admin/'  # redirect if not authorized
    # raise_exception = True   # exeption = if not authorized