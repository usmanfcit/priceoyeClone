from django import forms

from .models import Product, Category, Vendor
from django_extensions.db.models import ActivatorModel


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["deactivate_date"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.filter(status=ActivatorModel.ACTIVE_STATUS)
        self.fields["vendor"].queryset = Vendor.objects.filter(status=ActivatorModel.ACTIVE_STATUS)
