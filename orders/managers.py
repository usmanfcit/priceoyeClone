from django.db import models
from django_extensions.db.models import ActivatorModel


class OrderManager(models.Manager):
    def active(self):
        return self.filter(status=ActivatorModel.ACTIVE_STATUS)

    def inactive(self):
        return self.filter(status=ActivatorModel.INACTIVE_STATUS)
