from django.contrib import admin

from .forms import ProductForm
from .models import Product, Vendor, Category, SpecificationCategory, SpecificationDetail, SpecificationHeader


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "creation_date")
    list_editable = ("is_active",)


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "creation_date")
    list_editable = ("is_active",)


class SpecificationDetailInline(admin.TabularInline):
    model = SpecificationDetail
    extra = 1
    fields = ["header", "value"]
    readonly_fields = ["header", "value"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    inlines = [SpecificationDetailInline]


admin.site.register(SpecificationDetail)
admin.site.register(SpecificationHeader)
admin.site.register(SpecificationCategory)
