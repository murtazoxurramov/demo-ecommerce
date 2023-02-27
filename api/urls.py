from profile.views import VendorProfileViewSet, VendorProfileShopsViewSet, VendorProdileProducts

from django.urls import include, path
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenRefreshView

from product.views import ProductViewSet
from shop.views import ShopCategoryViewSet, ShopViewSet
from users.views import EmailOrPhoneTokenObtainPairView

router = routers.DefaultRouter()
router.register(
    r'shop-categories', ShopCategoryViewSet, basename='shop-categories'
)
router.register(
    r'shops', ShopViewSet, basename='shops'
)
router.register(
    r'products', ProductViewSet, basename='products'
)
router.register(
    r'vendor-profile', VendorProfileViewSet, basename='vendor-profile'
)

shop_router = routers.NestedDefaultRouter(
    router, r'vendor-profile', lookup='user'
)
shop_router.register(
    r'shops',
    VendorProfileShopsViewSet,
    basename='shops'
)

produc_router = routers.NestedDefaultRouter(
    shop_router, r'shops', lookup='shop'
)

produc_router.register(
    r'products',
    VendorProdileProducts,
    basename='products'
)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(shop_router.urls)),
    path('', include(produc_router.urls)),
    path('token/', EmailOrPhoneTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
