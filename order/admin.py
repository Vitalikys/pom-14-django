from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'created_at', 'end_at')
    list_filter = ('book', 'user', 'created_at')
    list_display_links = ('id', 'book')

    fields = ('book', 'user', 'created_at', ('end_at', 'plated_end_at')) #, 'authors'
    search_fields = ('id', 'book')
    readonly_fields = ('book', 'user', 'created_at')



# admin.site.register(Order)

admin.site.site_title = 'новинa Title admin'
admin.site.site_header = 'Керування Бібліотекою'