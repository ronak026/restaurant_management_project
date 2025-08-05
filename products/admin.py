from django.contrib import admin
from .models import *


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']
    search_field = ('name')

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    
admin.site.register(Item,ItemAdmin)
