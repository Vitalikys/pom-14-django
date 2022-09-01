from django.urls import include, path
from .views import *

urlpatterns = [
    path('', list_books, name = 'list_books'),
    path('detail_book/<int:id>/', detail_book, name='book_detail_url'),
]