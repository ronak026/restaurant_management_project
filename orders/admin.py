from django.contrib import admin
from .models import *

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model=OrderItem
    extra = 1 # how many blank order items to show on the order page

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','status','total_amount','created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__username',)
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)