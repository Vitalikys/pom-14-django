from django.contrib import admin

from book.models import Book
from author.models import Author
from order.models import Order
from authentication.models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'count')
    # list_display_links = ('id', 'name')
    list_editable = ( 'name',  'count')
    # fields = ('name', 'description', 'count') #, 'authors'
    save_on_top = True
    search_fields = ('id', 'name')

admin.site.register(Author)
# admin.site.register(Book)
admin.site.register(Order)
admin.site.register(CustomUser)
admin.site.site_title = 'Library team-28'