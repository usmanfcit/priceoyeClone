from django.urls import path

from . import views
app_name = "orders"
urlpatterns = [
    path("add-to-cart/<int:product_id>/", views.AddToCart.as_view(), name="add_to_cart"),
    path("delete-from-cart/<int:pk>/", views.DeleteProductFromCart.as_view(), name="delete_product_from_cart"),
    path("create-support-ticket/<int:order_id>/", views.CreateSupportTicket.as_view(), name="create_support_ticket"),
    path("show-cart/", views.ShowCart.as_view(), name="show_cart"),
    path("show-orders/", views.ShowOrders.as_view(), name="show_orders"),
    path("show-ticket-form/<int:pk>/", views.ShowTicketForm.as_view(), name="show_ticket_form"),
    path("list-support-tickets/", views.ListSupportTickets.as_view(), name="list_support_tickets"),
    path("finalize-order/<int:order_id>", views.FinalizeOrder.as_view(), name="finalize_order"),
]
