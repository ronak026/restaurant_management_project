from django.contrib import admin
from products.models import Item

# Custom Admins
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']
    search_fields = ('item_name',)

# Register your models here.
# admin.site.register(Item,ItemAdmin)
