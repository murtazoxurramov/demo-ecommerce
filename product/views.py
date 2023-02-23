from rest_framework import viewsets

from .models import Product
from .serializers import ProductDetailSerializer, ProductListSerializer


class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'title'):
            queryset = self.queryset.exclude(title__exact='')

        return queryset


class ProductModelViewSet(CustomModalViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = None
    http_method_names = ['get']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return self.serializer_class
