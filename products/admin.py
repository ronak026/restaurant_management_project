from django.contrib import admin
from .models import *


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']
    search_field = ('name')

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','customer_name','status','total_amount','created_at')
    search_field=('customer__username')
    filter_horizontal=('items')
    
admin.site.register(Item,ItemAdmin)
