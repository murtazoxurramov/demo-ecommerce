from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='SurxonBazar API',)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include('api.urls')),
    re_path("swagger/", schema_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
