from django.urls import path

from . import views


urlpatterns = [
    path("review-for-product/list/<int:object_id>/", views.ProductReviewListingAPIView.as_view()),
    path("review-for-vendor/list/<int:object_id>/", views.VendorReviewListingAPIView.as_view()),
    path("vendor-products/list/", views.VendorProductListingAPIView.as_view()),
]


