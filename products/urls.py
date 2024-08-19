from django.urls import path

from . import views

urlpatterns = [
    path("homepage/", views.Homepage.as_view(), name="homepage"),
    path("<str:category_name>/", views.ProductListingByCategory.as_view(), name="product_listing_by_category"),
    path("<str:category_name>/<int:pk>", views.ProductDetailsView.as_view(), name="product_detail")
]
