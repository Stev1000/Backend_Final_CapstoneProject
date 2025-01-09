# products/admin.py

from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Customize fields as needed
    search_fields = ('name',)
    list_filter = ('price',)
