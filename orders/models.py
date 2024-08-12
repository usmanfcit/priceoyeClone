from django.db import models

from products.models import Product
from users.models import User
from .status_choices import OrderStatusChoices, SupportTicketStatusChoices


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, choices=OrderStatusChoices.choices)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.user.email


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.product.name


class SupportTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=SupportTicketStatusChoices.choices,
        default=SupportTicketStatusChoices.OPEN
    )

    def __str__(self):
        return self.subject

