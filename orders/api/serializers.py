from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from orders.models import Order, OrderItem, SupportTicket
from users.models import User


class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ("order", "product", "quantity", "price")

    def get_price(self, obj):
        return obj.price

    def create(self, data):
        order = data["order"]
        product = data["product"]
        quantity = data["quantity"]

        order_item, created = OrderItem.objects.update_or_create(
            order=order,
            product=product,
            defaults={"quantity": quantity}
        )
        return order_item


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.active(),
        default=serializers.CurrentUserDefault()
    )
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ("id", "order_status", "items", "user", "created")

    def validate(self, attrs):
        if not self.context["request"].user.is_staff:
            raise ValidationError({"ValidationError": "You are not allowed to do this operation."})
        return super().validate(attrs)


class SupportTicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SupportTicket
        fields = "__all__"
