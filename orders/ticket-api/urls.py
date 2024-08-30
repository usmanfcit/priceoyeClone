from django.urls import path
from . import views

urlpatterns = [
    path("list-or-create", views.SupportTicketListCreateAPIView.as_view()),
    path("update-or-delete/<int:pk>", views.SupportTicketUpdateDestroyAPIView.as_view()),
]
