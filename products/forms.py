from django import forms
from django.contrib import admin

from .models import Product, Category, Vendor


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.filter(is_active=True)
        self.fields["vendor"].queryset = Vendor.objects.filter(is_active=True)
