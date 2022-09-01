from django.urls import include, path
from .views import *

urlpatterns = [
    path('', list_author, name='list_author'),
    # path('add_author/', CreateAuthor.as_view(), name = 'add_author')
    path('add_author/', add_author, name = 'add_author'),
    path('delete_author/<int:id>', delete_author, name = 'author_delete_url'),

]
