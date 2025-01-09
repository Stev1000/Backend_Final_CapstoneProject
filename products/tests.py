from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product, Category


class ProductAPITestCase(TestCase):
    def setUp(self):
        # Initialize the API client
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a test category
        self.category = Category.objects.create(name='Electronics', description='Electronic products')

        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            description='A product for testing',
            price=10.99,
            category=self.category,
            stock_quantity=100,
            image_url='http://example.com/image.jpg'
        )

    def test_get_products_list(self):
        # Test the GET list endpoint
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_product_unauthenticated(self):
        # Test creating a product without authentication
        data = {
            'name': 'New Product',
            'description': 'Description',
            'price': 20.00,
            'category_id': self.category.id,  # Use 'category_id'
            'stock_quantity': 50,
            'image_url': 'http://example.com/image.jpg'
        }
        response = self.client.post('/api/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Expect 401 Unauthorized

    def test_create_product_authenticated(self):
        # Test creating a product with authentication
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'New Product',
            'description': 'Description',
            'price': 20.00,
            'category_id': self.category.id,  # Use 'category_id'
            'stock_quantity': 50,
            'image_url': 'http://example.com/image.jpg'
        }
        response = self.client.post('/api/products/', data, format='json')
        
        # Debug: Print the response data
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Expect 201 Created
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.get(id=response.data['id']).name, 'New Product')

    def test_update_product_authenticated(self):
        # Test updating a product with authentication
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'Updated Product',
            'description': 'Updated Description',
            'price': 15.99,
            'category_id': self.category.id,  # Use 'category_id'
            'stock_quantity': 80,
            'image_url': 'http://example.com/updated_image.jpg'
        }
        response = self.client.put(f'/api/products/{self.product.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Expect 200 OK
        self.assertEqual(Product.objects.get(id=self.product.id).name, 'Updated Product')

    def test_delete_product_authenticated(self):
        # Test deleting a product with authentication
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Expect 204 No Content
        self.assertEqual(Product.objects.count(), 0)

    def test_search_products(self):
        # Test searching for products
        response = self.client.get('/api/products/?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Expect 200 OK
        self.assertEqual(len(response.data['results']), 1)

    def test_filter_products_by_category(self):
        # Test filtering products by category name
        response = self.client.get(f'/api/products/?category__name={self.category.name}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Expect 200 OK
        self.assertEqual(len(response.data['results']), 1)
