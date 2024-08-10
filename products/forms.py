from django import forms

from .models import Product, Category, Vendor


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["vendor"].queryset = Vendor.objects.active()
        self.fields["category"].queryset = Category.objects.active()

    class Meta:
        model = Product
        exclude = ["deactivate_date"]
