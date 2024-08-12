from django.utils.translation import gettext_lazy as _
from django.db import models


class OrderStatusChoices(models.TextChoices):
    ORDER_PLACED = "order_placed", _("Order_Placed")
    UNDER_PROCESSING = "under_processing", _("under_processing")
    DISPATCHED = "dispatched", _("Dispatched")
    DELIVERED = "delivered", _("Delivered")


class SupportTicketStatusChoices(models.TextChoices):
    OPEN = "open", _("Open")
    IN_PROGRESS = "in_progress", _("In_progress")
    RESOLVED = "resolved", _("Resolved")
    CLOSED = "closed", _("Closed")
