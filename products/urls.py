from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserViewSet

app_name = 'products'

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),  # Ensure the router URLs are included
]
