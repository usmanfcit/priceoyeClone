from django.contrib import admin

from .models import Product, Vendor, Category

admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Category)
