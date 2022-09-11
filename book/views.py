from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView

from rest_framework import generics, mixins
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.permission import IsAdminOrReadOnly
from.serializers import BookSerializer
from .models import Book
from .forms import BookForm

# class BookAPIView(generics.ListCreateAPIView, mixins.ListModelMixin,
#                   mixins.CreateModelMixin, mixins.UpdateModelMixin,
#                   mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     queryset = Book.objects.all()
#     lookup_field = 'id'
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # permission_classes = (IsAuthenticated, IsAdminOrReadOnly)
#     serializer_class = BookSerializer
#     def get(self, request, id = None):
#         if id: return self.retrieve(request)
#         else: return self.list(request)
#     def post(self, request, *args, **kwargs):
#         return self.create(request)
#     def put(self,request, id =None):
#         return self.update(request, id)
#     def delete(self,request, id):
#         return self.destroy(request, id)


class BookAPIView(APIView):
# class BookAPIView(generics.ListCreateAPIView):
#     # permission_classes = (IsAuthenticated,)
#     # authentication_classes = (TokenAuthentication,)
    queryset = Book.objects.all().values()
    def get(self, request, id = None):
        if id:
            book= Book.get_by_id(id)
            return Response({'one book from GET':BookSerializer(book).data})
        else:
            lst = Book.objects.all()
            return Response({'all books from GET':BookSerializer(lst, many=True).data})
    def post(self, request):
        from django.forms import model_to_dict
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # post_new = Book.objects.create(
        #     name=request.data['name'],
        #     description=request.data['description'],
        #     count=request.data['count'],
        #     authors=request.data['authors']
        # )
        return Response({'post': serializer.data})
        # return Response({'post': BookSerializer(post_new).data})
    def put(self,request, *args, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            return Response({'error': "method PUT not allowed here, no ID"})
        try:
            book_to_update = Book.get_by_id(id)
        except:
            return Response({'error': "method PUT, Book not Found"})
        serializer = BookSerializer(data=request.data, instance=book_to_update)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"post":serializer.data})

    def delete(self,request,*args, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            return Response({'error': "method DELETE not allowed here, no ID"})
        try:
            book_to_delete = Book.get_by_id(id)
        except:
            return Response({'error': "method DELETE, Book not Found"})
        book_to_delete.delete()
        return Response({"post":"Delete book id = " +str(id)})

# class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = [IsAuthenticated, IsLibrarian]
#     serializer_class = BookSerializer
#     queryset = Book.get_all()



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
