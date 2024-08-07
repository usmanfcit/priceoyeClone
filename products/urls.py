from django.urls import path

from . import views

urlpatterns = [
    path("homepage/", views.homepage, name="homepage"),
    path("<str:category_name>/", views.category_product_page, name="category_products"),
    path("<str:category_name>/<int:product_id>", views.product_details, name="product_details")
]
