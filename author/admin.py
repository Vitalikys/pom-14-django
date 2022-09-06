from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic')
    list_filter = ('id', 'name', 'surname')
    # list_editable = ( 'name',  'count')
    # fields = ('name', 'description', 'count') #, 'authors'
    save_on_top = True
    search_fields = ('name', 'surname')

# admin.site.register(Author)
