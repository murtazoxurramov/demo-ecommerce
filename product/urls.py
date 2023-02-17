from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ProductCategoryModelViewSet, ProductModelViewSet

router = DefaultRouter()
router.register(r'product-categories', ProductCategoryModelViewSet)
router.register(r'products', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
