from django.contrib import admin
from django.urls import include, path

from products.views import homepage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("products/", include("products.urls")),
    path("orders/", include("orders.urls", namespace='orders')),
    path("", homepage),
]
