from django.db import models
from django_extensions.db.models import TimeStampedModel, ActivatorModel

from .managers import ProductManager, CategoryManager, VendorManager


class Category(TimeStampedModel, ActivatorModel):
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    objects = CategoryManager()

    def __str__(self):
        return self.name


class Vendor(TimeStampedModel, ActivatorModel):
    name = models.CharField(max_length=40, unique=True)

    objects = VendorManager()

    def __str__(self):
        return self.name


class SpecificationCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Specification Categories"

    def __str__(self):
        return self.name


class ProductSpecificationCategory(models.Model):
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="specification_categories"
    )
    specification_category = models.ForeignKey(
        SpecificationCategory,
        on_delete=models.CASCADE,
        related_name="product"
    )

    class Meta:
        verbose_name_plural = "Product Specification Categories"

    def __str__(self):
        return f"{self.product.name} - {self.specification_category.name}"


class SpecificationDetail(models.Model):
    specification_category = models.ForeignKey(
        ProductSpecificationCategory,
        on_delete=models.CASCADE,
        related_name="details")
    specification_label = models.CharField(max_length=100)
    specification_value = models.TextField()

    def __str__(self):
        return f"{self.specification_label}: {self.specification_value}"


class Product(TimeStampedModel, ActivatorModel):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)

    objects = ProductManager()

    def __str__(self):
        return self.name
