from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api import views
from products.views import Homepage


def trigger_error(request):
    division_by_zero = 1 / 0


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'vendors', views.VendorViewSet)

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("users/", include("users.urls")),
                  path("api/", include("users.api.urls")),
                  path("products/", include("products.urls")),
                  path("orders/", include("orders.urls", namespace='orders')),
                  path('sentry-debug/', trigger_error),
                  path("", Homepage.as_view()),
                  path("product-api/", include(router.urls)),
                  path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
              ] + debug_toolbar_urls()
