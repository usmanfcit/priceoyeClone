from rest_framework import generics
from rest_framework.response import Response

from orders.api.serializers import OrderSerializer, OrderItemSerializer
from orders.models import OrderItem, Order
from orders.status_choices import OrderStatusChoices


class OrderCreationAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class OrderItemCreationAPIView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer


class OrderItemDeletionAPIView(generics.DestroyAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return OrderItem.objects.filter(order__user=self.request.user)


class OrderItemUpdateAPIView(generics.UpdateAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return OrderItem.objects.filter(order__user=self.request.user)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.quantity != request.data['quantity']:
            instance.price = instance.product.price * request.data['quantity']
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class OrderDeletionAPIView(generics.DestroyAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user,
            order_status__in=[OrderStatusChoices.ORDER_PLACED, OrderStatusChoices.IN_CART]
        )


class OrderUpdateAPIView(generics.UpdateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderListingAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
