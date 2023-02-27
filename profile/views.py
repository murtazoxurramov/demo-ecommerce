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


class VendorProfileShopsViewSet(CustomModalViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopListSerializer

    def list(self, request, user_pk=None):
        obj = Shop.objects.filter(owner=user_pk).prefetch_related('owner')
        data = ShopListSerializer(obj, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    def retrieve(self, request, user_pk=None, pk=None):
        obj = Shop.objects.filter(owner=user_pk).prefetch_related(
            'owner').filter(pk=pk)
        if obj.exists():
            data = ShopDetailSerializer(obj, many=True).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data = {'Message': "Not Foud"}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)


class VendorProdileProducts(CustomModalViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def list(self, request, user_pk=None, shop_pk=None):
        obj = self.queryset.filter(shop=shop_pk).prefetch_related('shop')
        data = self.serializer_class(obj, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    def retrieve(self, request, user_pk=None, shop_pk=None, pk=None):
        obj = self.queryset.filter(shop=shop_pk).prefetch_related(
            'shop').filter(pk=pk)
        if obj.exists():
            data = ProductDetailSerializer(obj, many=True).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data = {'Message': "Not Foud"}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
