from rest_framework import viewsets

from .serializers import VendorProfileSerializer, VendorShopListSerializer, VendorShopDetailSerializer
from .models import VendorProfile


class VendorProfileViewSet(viewsets.ModelViewSet):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer
    pagination_class = None
    http_method_names = ['get']


class VendorShopListViewSet(viewsets.ModelViewSet):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorShopListSerializer
    pagination_class = None
    http_method_names = ['get']


class VendorShopDetailViewSet(viewsets.ModelViewSet):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorShopDetailSerializer
    pagination_class = None
    http_method_names = ['get']
