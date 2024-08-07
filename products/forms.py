from django import forms

from .models import Product, Category, Vendor


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["deactivate_date"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.filter(status=1)
        self.fields["vendor"].queryset = Vendor.objects.filter(status=1)
