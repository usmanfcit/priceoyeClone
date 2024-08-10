from django.urls import path

from . import views

urlpatterns = [
    path("homepage/", views.homepage, name="homepage"),
    path("<str:category_name>/", views.product_listing_by_category, name="category_products"),
    path("<str:category_name>/<int:product_id>", views.product_detail, name="product_detail")
]
