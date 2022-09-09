from django.contrib import admin
from .models import Item

class ToDoItem(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_display_links = ('name', 'description')
    search_fields = ('name', 'description', 'price')
    list_editable = ('price',)
    list_filter = ('price',)

admin.site.register(Item, ToDoItem)