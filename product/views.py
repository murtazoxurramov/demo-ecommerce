from rest_framework import viewsets

from .models import Product, ProductCategory
from .serializers import ProductCategorySerializer, ProductMainSerializer, ProductDetailSerializer

class CustomModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset

        return queryset


class ProductCategoryModelViewSet(CustomModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = None
    http_method_names = ['get']


class ProductModelViewSet(CustomModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductMainSerializer
    pagination_class = None
    http_method_names = ['get']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return self.serializer_class


