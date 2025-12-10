"""Views for Products API."""
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for Product model."""
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

    def get_queryset(self):
        """Filter active products."""
        return Product.objects.filter(is_active=True).order_by('-created_at')
