from django.db import models
from django_extensions.db.models import ActivatorModel


class ProductManager(models.Manager):
    def active(self):
        return self.filter(status=ActivatorModel.ACTIVE_STATUS)

    def inactive(self):
        return self.filter(status=ActivatorModel.INACTIVE_STATUS)

    def by_status(self, status):
        return self.filter(status=status)


class VendorManager(models.Manager):
    def active(self):
        return self.filter(status=ActivatorModel.ACTIVE_STATUS)

    def inactive(self):
        return self.filter(status=ActivatorModel.INACTIVE_STATUS)

    def by_status(self, status):
        return self.filter(status=status)


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=ActivatorModel.ACTIVE_STATUS)

    def inactive(self):
        return self.filter(status=ActivatorModel.INACTIVE_STATUS)

    def by_status(self, status):
        return self.filter(status=status)
