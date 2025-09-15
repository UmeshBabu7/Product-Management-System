from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku', 'name', 'category', 'price', 'stock_qty', 'status', 'created_at']
    list_filter = ['category', 'status', 'created_at']
    search_fields = ['sku', 'name', 'category']
    list_editable = ['price', 'stock_qty', 'status']
    list_per_page = 25
    ordering = ['sku']
    
    fieldsets = (
        ('Product Information', {
            'fields': ('sku', 'name', 'category')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'stock_qty', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()

