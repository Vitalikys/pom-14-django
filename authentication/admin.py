from django.contrib import admin


from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'middle_name', 'email', 'role')
    list_display_links = ('id', 'first_name')
    # list_editable = ( 'name',  'count')
    # fields = ('name', 'description', 'count') #, 'authors'
    save_on_top = True
    search_fields = ('id', 'first_name')

# admin.site.register(CustomUser)