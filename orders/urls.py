from django.urls import path

from . import views
app_name = "orders"
urlpatterns = [
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("delete-from-cart/<int:product_id>/", views.delete_product_from_cart, name="delete_product_from_cart"),
    path("create-support-ticket/<int:order_id>/", views.create_support_ticket, name="create_support_ticket"),
    path("show-cart/", views.show_cart, name="show_cart"),
    path("show-ticket-form/<int:order_id>/", views.show_ticket_form, name="show_ticket_form"),
    path("show-support-ticket/", views.show_support_ticket, name="show_support_ticket"),
]
