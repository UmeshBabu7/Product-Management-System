from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    is_in_stock = serializers.ReadOnlyField()
    is_active = serializers.ReadOnlyField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'sku', 'name', 'category', 'price', 
            'stock_qty', 'status', 'is_in_stock', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
