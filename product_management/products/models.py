from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Product(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    CATEGORY_CHOICES = [
        ('Clothing', 'Clothing'),
        ('Electronics', 'Electronics'),
        ('Home', 'Home'),
        ('Sports', 'Sports'),
        ('Books', 'Books'),
        ('Beauty', 'Beauty'),
    ]
    
    sku = models.CharField(max_length=50, unique=True, verbose_name="SKU")
    name = models.CharField(max_length=200, verbose_name="Product Name")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Category")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Price"
    )
    stock_qty = models.PositiveIntegerField(verbose_name="Stock Quantity")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['sku']
    
    def __str__(self):
        return f"{self.sku} - {self.name}"
    
    @property
    def is_in_stock(self):
        """Check if product is in stock"""
        return self.stock_qty > 0
    
    @property
    def is_active(self):
        """Check if product is active"""
        return self.status == 'active'

