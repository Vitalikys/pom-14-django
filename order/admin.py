from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_name','book', 'user', 'created_at', 'end_at')
    list_filter = ('book', 'user', 'created_at')
    list_display_links = ('id', 'book')

    fields = ('book','get_user_name', 'user', 'created_at', ('end_at', 'plated_end_at')) #, 'authors'
    search_fields = ('id', 'book')
    readonly_fields = ('book', 'user', 'created_at')

    @admin.display(description='User_: ')
    def get_user_name(self, obj):
        user = obj.user
        return f'{user.first_name} {user.last_name}'



# admin.site.register(Order)

admin.site.site_title = 'новинa Title admin'
admin.site.site_header = 'Керування Бібліотекою'