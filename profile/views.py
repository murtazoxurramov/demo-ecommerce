from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductListSerializer
from shop.models import Shop

from .models import VendorProfile
from .serializers import (VendorProfileSerializer,
                          VendorProfileShopListSerializer,
                          VendorProfileShopSerializer)


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
        queryset = VendorProfile.objects.all()
        data = VendorProfileShopListSerializer(queryset, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='shops/(?P<shop_id>[^/.]+)')
    def shop_detail(self, request, pk=None, shop_id=None):
        data = VendorProfileShopSerializer(shop_id, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class VendorProfileShopDetailViewSet(CustomModalViewSet):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileShopSerializer
    pagination_class = None
    http_method_names = ['get']

    # @action(methods=['get'], detail=True)
    # def shops(self, request, pk=None):
    #     queryset = VendorProfile.objects.all()
    #     data = VendorProfileShopSerializer(queryset, many=True).data
    #     return Response(data=data, status=status.HTTP_200_OK)
