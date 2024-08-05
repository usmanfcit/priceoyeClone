from django.db import models
import json


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Specifications(models.Model):
    specifications = models.JSONField()

    def __str__(self):
        return json.dumps(self.specifications)


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    specifications = models.ForeignKey(Specifications, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
