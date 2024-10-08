from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from priceoyeclone import settings
from products.views import Homepage


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("users/", include("users.urls")),
                  path("api/user/", include("users.api.urls")),
                  path("api/order/", include("orders.api.urls")),
                  path("api/product/", include("products.api.urls")),
                  path("products/", include("products.urls")),
                  path("orders/", include("orders.urls", namespace="orders")),
                  path("sentry-debug/", trigger_error),
                  path("", Homepage.as_view()),
                  path("gettoken/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
                  path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
                  path("token/verify/", TokenVerifyView.as_view(), name="token_refresh"),
              ] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
