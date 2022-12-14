from django.urls import include, path
from .views import *

urlpatterns = [
    path('', list_author, name='list_author'),
    # path('add_author/', CreateAuthor.as_view(), name = 'add_author')
    path('add_author/', add_author, name = 'add_author'),
    path('delete_author/<int:id>', delete_author, name = 'author_delete_url'),
    path('change_author/<int:id>', edit, name = 'change_author_url'),
    # path('change_author/<int:pk>', UpdateAuthorView.as_view(), name = 'change_author_url'),


    # path('api/v1/author/', AuthorListCreateView.as_view()),
    # path('api/v1/author/<int:pk>/', AuthorListDetailView.as_view()),
    # path('api/v1/authordelete/<int:pk>/', AuthorAPIDestroyView.as_view()),
]
