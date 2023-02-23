from rest_framework import viewsets

from .models import Shop, ShopCategory
from .serializers import (ShopCategorySerializer, ShopDetailSerializer,
                          ShopListSerializer)


class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'title'):
            queryset = self.queryset.exclude(title__exact='')

        return queryset


class ShopCategoryViewSet(CustomModalViewSet):
    queryset = ShopCategory.objects.filter(parent__isnull=True)
    serializer_class = ShopCategorySerializer
    pagination_class = None
    http_method_names = ['get']


class ShopViewSet(CustomModalViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopListSerializer
    pagination_class = None
    http_method_names = ['get']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ShopDetailSerializer
        return self.serializer_class
