from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from product.views import ProductModelViewSet
from users.views import EmailOrPhoneTokenObtainPairView
from shop.views import ShopCategoryViewSet, ShopViewSet
from profile.views import VendorProfileViewSet, VendorShopListViewSet, VendorShopDetailSerializer

router = DefaultRouter()
router.register(r'shop-categories', ShopCategoryViewSet, basename='shop-categories')
router.register(r'shops', ShopViewSet, basename='shops')
router.register(r'products', ProductModelViewSet, basename='products')
router.register(r'vendor-profile', VendorProfileViewSet, basename='vendor-profile')
router.register(r'^vendor-profile/shops/(?P<pk>.+)/$', VendorShopListViewSet, basename='vendor-shops')
# router.register(r'vendor-profile/shops/{pk}/products', VendorShopDetailSerializer)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', EmailOrPhoneTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
