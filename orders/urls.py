from django.urls import path

from . import views
app_name = "orders"
urlpatterns = [
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("delete-from-cart/<int:product_id>/", views.delete_product_from_cart, name="delete_product_from_cart"),
    path("show-cart/", views.show_cart, name="show_cart"),
]
