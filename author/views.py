from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Author
from .forms import AddAuthorForm
def list_author(request):
    return render(request, 'author/author_list.html', {'author': Author.get_all() } )

def add_author(request):
    if request.method == 'POST':
        form= AddAuthorForm(request.POST) # забираємо дані
        if form.is_valid():
            form.save()
            return redirect('list_author')
    else:
        form = AddAuthorForm() #створ екземпл пустої форми
    return render(request, 'author/add_author.html', {'form':form} )

# class CreateAuthor(CreateView):
#     form_class = AddAuthorForm
    template_name = 'author/add_author.html'
    # login_url = 'admin/'  # redirect if not authorized
    # raise_exception = True   # exeption = if not authorized