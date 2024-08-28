from django.urls import path
from . import views

urlpatterns = [
    path("create", views.OrderCreationAPIView.as_view()),
    path("add-item-to-order", views.OrderItemCreationAPIView.as_view()),
    path("delete-item-from-order/<int:pk>", views.OrderItemDeletionAPIView.as_view()),
    path("update-item-from-order/<int:pk>", views.OrderItemUpdateAPIView.as_view()),
    path("delete-order/<int:pk>", views.OrderDeletionAPIView.as_view()),
    path("update-order/<int:pk>", views.OrderUpdateAPIView.as_view()),
    path("list-orders", views.OrderListingAPIView.as_view()),
    ]
