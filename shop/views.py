from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, status, response
from .models import Category, Shop
from .serializers import (CategorySerializer, ShopDetailSerializer,
                          ShopListSerializer)


class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'title'):
            queryset = self.queryset.exclude(title__exact='')

        return queryset


class ShopCategoryViewSet(CustomModalViewSet):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer
    pagination_class = None
    http_method_names = ['get']


class ShopViewSet(CustomModalViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopListSerializer
    pagination_class = None
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ShopDetailSerializer
        return self.serializer_class
