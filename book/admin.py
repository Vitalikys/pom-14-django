from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'count', 'author')
    list_filter = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    list_editable = ('count',)
    # fields = ('name', 'description', 'count') #, 'authors'
    save_on_top = True
    search_fields = ('id', 'name')
    fieldsets = (
        (None, {
             'fields': ( 'name','authors' )
        }),
        ('Changable options:', {
            'fields': ('description', 'count'),
        }),
    )


    def author(self, obj):
        return [i.name for i in obj.authors.all()]

# admin.site.register(Book)
