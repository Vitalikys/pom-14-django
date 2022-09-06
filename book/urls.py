from django.urls import include, path
from .views import *

urlpatterns = [
    path('', list_books, name = 'list_books'),
    path('detail_book/<int:id>/', detail_book, name='book_detail_url'),
    path('edit_book/<int:id>', change_book, name='edit_book'),
    path('delete_book/<int:id>', delete_book, name='delete_book'),
    path('add_book/', AddBook.as_view(), name='add_book'),
    # path('delete_author/<int:id>', delete_author, name='author_delete_url'),

]