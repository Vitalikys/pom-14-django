from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from .models import Author
from .forms import AddAuthorForm

class UpdateAuthorView(UpdateView):
    model = Author #.get_form_kwargs()
    template_name = 'author/edit_author.html'
    fields = ('name', 'surname', 'patronymic' )

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

# def change_author(request, id=0):
#     try:
#         if request.method == 'GET':
#             if id ==0:
#                 form = AddAuthorForm()
#             else:
#                 author = Author.get_by_id(id)
#                 form = AddAuthorForm(request.POST or None, instance=author)
#                 # form = AddAuthorForm(initial=dict(field_name=get_form_kwargs)
#                 context = {'form': form, 'author':author}
#             return render(request, 'author/edit_author.html', context=context)
#         else:
#         # elif request.method == 'POST':
#             if id==0:
#                 form = AddAuthorForm(request.POST)
#             else:
#                 author = Author.get_by_id(id)
#                 form = AddAuthorForm(request.POST, instance=author)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, f'Changed new author: {author.surname} success !')
#             else:
#                 return render(request, 'author/edit_author.html', {'form': form})
#             return redirect('list_author')
#     except Exception:
#         messages.error(request, f'You catch error!')

@login_required
def edit(request, id=None, template_name='author/edit_author.html'):
    if id:
        author = Author.get_by_id(id)
        # author = get_object_or_404(Author, pk=id)
    form = AddAuthorForm(request.POST or None, instance=author)
    if request.POST and form.is_valid():
        form.save()

        # Save was successful, so redirect to another page
        messages.success(request, f'Changes to author: {author.name} success !')
        return redirect('list_author')
    context = {'form': form, 'author': author}
    return render(request, template_name, context=context)


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