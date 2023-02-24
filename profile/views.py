from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductDetailSerializer, ProductListSerializer
from shop.models import Shop
from shop.serializers import ShopDetailSerializer, ShopListSerializer

from .models import VendorProfile
from .serializers import VendorProfileSerializer


class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'title'):
            queryset = self.queryset.exclude(title__exact='')

        return queryset


class VendorProfileViewSet(CustomModalViewSet):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer
    pagination_class = None
    http_method_names = ['get']

    @action(methods=['get'], detail=True)
    def shops(self, request, pk=None):
        queryset = Shop.objects.filter(owner=pk)
        data = ShopListSerializer(queryset, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['get', 'post'], detail=True, url_path='shops/(?P<shop_id>[^/.]+)')
    def shop_detail(self, request, pk=None, shop_id=None):
        obj = Shop.objects.filter(pk=shop_id)
        data = ShopDetailSerializer(obj, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='shops/(?P<shop_id>[^/.]+)/products')
    def products(self, request, pk=None, shop_id=None):
        queryset = Product.objects.filter(shop=shop_id)
        data = ProductListSerializer(queryset, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['get', 'post'], detail=True, url_path='shops/(?P<shop_id>[^/.]+)/products/(?P<product_id>[^/.]+)')
    def product_detail(self, request, pk=None, shop_id=None, product_id=None):
        queryset = Product.objects.filter(pk=product_id)
        data = ProductDetailSerializer(queryset, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
