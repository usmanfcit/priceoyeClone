from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from orders.models import SupportTicket
from .serializers import SupportTicketSerializer


class SupportTicketListCreateAPIView(ListCreateAPIView):
    serializer_class = SupportTicketSerializer

    def get_queryset(self):
        return SupportTicket.objects.filter(user=self.request.user)


class SupportTicketUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SupportTicketSerializer

    def get_queryset(self):
        return SupportTicket.objects.filter(user=self.request.user)
