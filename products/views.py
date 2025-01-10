from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer, UserSerializer
from django.contrib.auth.models import User

class ProductViewSet(viewsets.ModelViewSet):
    # Use selective data retrieval for efficiency
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # Add filters, search, and ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description', 'category__name']  # Allow searching by product name, description, and category name
    ordering_fields = ['price', 'created_date']  # Allow ordering by price and creation date
    filterset_fields = ['category__name']  # Filter products by category name


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.only('id', 'username', 'email').all()  # Retrieve only necessary fields
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
