from rest_framework import generics

from orders.api.serializers import OrderSerializer, OrderItemSerializer
from orders.models import OrderItem, Order
from orders.status_choices import OrderStatusChoices
from .permissions import IsOwner, IsOrderOwner


class OrderCreationAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class OrderItemCreationAPIView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer


class OrderItemDeletionAPIView(generics.DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsOwner,)


class OrderDeletionAPIView(generics.DestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsOrderOwner,)

    def get_queryset(self):
        return Order.objects.filter(
            order_status__in=[OrderStatusChoices.ORDER_PLACED, OrderStatusChoices.IN_CART]
        )


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsOrderOwner,)


class OrderListingAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.active().filter(user=self.request.user)
