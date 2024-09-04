from django.urls import path

from . import views


urlpatterns = [
    path("review-for-product/list/<int:object_id>/", views.ProductReviewListingAPIView.as_view()),
    path("review-for-vendor/list/<int:object_id>/", views.VendorReviewListingAPIView.as_view()),
    path("list/", views.ProductListingAPIView.as_view()),
    path("add/", views.AddProductAPIView.as_view()),
    path("update/<int:pk>/", views.UpdateProductAPIView.as_view()),
    path("delete/<int:pk>/", views.DeleteProductAPIView.as_view()),
    path("add-vendor/", views.AddVendorAPIView.as_view()),
    path("update-vendor/<int:pk>/", views.UpdateVendorAPIView.as_view()),
    path("delete-vendor/<int:pk>/", views.DeleteVendorAPIView.as_view()),
    path("add-category/", views.AddCategoryAPIView.as_view()),
    path("update-category/<int:pk>/", views.UpdateCategoryAPIView.as_view()),
    path("delete-category/<int:pk>/", views.DeleteCategoryAPIView.as_view()),
]


