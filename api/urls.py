from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from product.views import ProductModelViewSet
from users.views import EmailOrPhoneTokenObtainPairView
from shop.views import ShopCategoryViewSet, ShopViewSet

router = DefaultRouter()
router.register(r'shop-categories', ShopCategoryViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'products', ProductModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', EmailOrPhoneTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
