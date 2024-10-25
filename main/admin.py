from django.contrib import admin
from .models import Product, Order, OrderItem

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    inlines = [OrderItemInline]
    readonly_fields = ('created_at',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
