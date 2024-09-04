from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel, ActivatorModel

from products.models import Product
from .managers import OrderManager
from .status_choices import OrderStatusChoices, SupportTicketStatusChoices

User = get_user_model()


class Order(TimeStampedModel, ActivatorModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.CharField(
        max_length=20,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.IN_CART
    )

    @property
    def total_price(self):
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return self.user.email + ' - ' + str(self.id)

    object = OrderManager()


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name + " - " + str(self.id)


class SupportTicket(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=SupportTicketStatusChoices.choices,
        default=SupportTicketStatusChoices.OPEN
    )

    def __str__(self):
        return self.title + " " + str(self.id)
