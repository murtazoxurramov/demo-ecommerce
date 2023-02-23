from profile.views import VendorProfileShopDetailViewSet, VendorProfileViewSet

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from product.views import ProductModelViewSet
from shop.views import ShopCategoryViewSet, ShopViewSet
from users.views import EmailOrPhoneTokenObtainPairView

router = DefaultRouter()
router.register(
    r'shop-categories', ShopCategoryViewSet, basename='shop-categories'
)
router.register(
    r'shops', ShopViewSet, basename='shops'
)
router.register(
    r'products', ProductModelViewSet, basename='products'
)
router.register(
    r'vendor-profile', VendorProfileViewSet, basename='vendor-profile'
)
# router.register(
#     r'vendor-profile/{pk}/shops', VendorProfileShopDetailViewSet, basename='vendor-shop'
# )


urlpatterns = [
    path('', include(router.urls)),
    path('token/', EmailOrPhoneTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
