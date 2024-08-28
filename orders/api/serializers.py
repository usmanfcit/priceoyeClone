from rest_framework import serializers

from orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("order", "product", "quantity")

    def create(self, data):
        order = data["order"]
        product = data["product"]
        quantity = data["quantity"]
        price = product.price * quantity

        order_item = OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price,
        )
        return order_item


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
