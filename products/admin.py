from django.contrib import admin

from .forms import ProductForm
from .models import (Product,
                     Vendor,
                     Category,
                     SpecificationCategory,
                     SpecificationDetail,
                     ProductSpecificationGroup
                     )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ["deactivate_date"]
    list_display = ("name", "status", "created", "modified")
    list_editable = ("status",)


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    exclude = ["deactivate_date"]
    list_display = ("name", "status", "created", "modified")
    list_editable = ("status",)


class SpecificationDetailInline(admin.TabularInline):
    model = SpecificationDetail
    extra = 0
    readonly_fields = ["specification_label", "specification_value"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    readonly_fields = ["created", "modified", "specification_groups"]


@admin.register(SpecificationDetail)
class SpecificationDetailAdmin(admin.ModelAdmin):
    readonly_fields = ["specification_group"]


admin.site.register(SpecificationCategory)
admin.site.register(ProductSpecificationGroup)
