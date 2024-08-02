from django.utils.translation import gettext_lazy as _
from django.db import models


class RoleChoices(models.TextChoices):
    CUSTOMER = "customer", _("Customer")
    STAFF = "staff", _("Staff")
    ADMIN = "admin", _("Admin")
