from django.utils.translation import gettext_lazy as _
from django.db import models


class OrderStatusChoices(models.TextChoices):
    ORDER_RECEIVED = "order_received", _("Order_received")
    UNDER_PROCESSING = "under_processing", _("under_processing")
    DISPATCHED = "Dispatched", _("Dispatched")
    DELIVERED = "Delivered", _("Delivered")
