from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)  # Index for frequent lookups
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)  # Indexed for faster searches
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)  # Index for sorting or range queries
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', db_index=True)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)  # Indexed for sorting by creation time
    updated_date = models.DateTimeField(auto_now=True, db_index=True)  # Indexed for tracking updates

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
