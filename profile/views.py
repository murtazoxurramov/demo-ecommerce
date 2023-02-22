from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductListSerializer
from shop.models import Shop

from .models import VendorProfile
from .serializers import VendorProfileSerializer


class VendorProfileViewSet(viewsets.ModelViewSet):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer
    pagination_class = None
    http_method_names = ['get']


# class VendorShopListViewSet(viewsets.ModelViewSet):
#     queryset = VendorProfile.objects.all()
#     serializer_class = VendorShopListSerializer
#     pagination_class = None
#     http_method_names = ['get']


# class VendorShopDetailViewSet(viewsets.ModelViewSet):
#     queryset = VendorProfile.objects.all()
#     serializer_class = VendorShopDetailSerializer
#     pagination_class = None
#     http_method_names = ['get']

#     @action(detail=True, methods=['get'])
#     def get_products(self, request, pk=None):
#         user = self.get_queryset()
#         shop = Shop.objects.filter(owner=user)
#         product = Product.objects.filter(shop=shop)
#         serializer = ProductListSerializer(product, many=True).data
#         return Response(serializer.data)
