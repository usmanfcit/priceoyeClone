from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.OrderCreationAPIView.as_view()),
    path("add-item/", views.OrderItemCreationAPIView.as_view()),
    path("remove-item/<int:pk>/", views.OrderItemDeletionAPIView.as_view()),
    path("delete/<int:pk>/", views.OrderDeletionAPIView.as_view()),
    path("update/<int:pk>/", views.OrderUpdateAPIView.as_view()),
    path("list/", views.OrderListingAPIView.as_view()),
    path("supportticket/list-or-create/", views.SupportTicketListCreateAPIView.as_view()),
    path("supportticket/update-or-delete/<int:pk>/", views.SupportTicketUpdateDestroyAPIView.as_view()),
    path("filtered-listing/", views.OrderListingByStatusAPIView.as_view())
    ]
