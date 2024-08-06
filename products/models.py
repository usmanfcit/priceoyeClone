from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_default_pk(cls):
        no_category, created = cls.objects.get_or_create(
            name="No Category",
        )
        return no_category.pk

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SpecificationCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Specification Categories"

    def __str__(self):
        return self.name


class SpecificationHeader(models.Model):
    category = models.ForeignKey(SpecificationCategory, on_delete=models.CASCADE, related_name="headers")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class SpecificationDetail(models.Model):
    header = models.ForeignKey(SpecificationHeader, on_delete=models.CASCADE, related_name="details")
    value = models.TextField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="specifications")

    def __str__(self):
        return f"{self.header.name}: {self.value}"


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        default=Category.get_default_pk,
        null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
