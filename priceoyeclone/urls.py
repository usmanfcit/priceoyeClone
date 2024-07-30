from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("priceoye_clone_app/", include("priceoye_clone_app.urls")),
]
