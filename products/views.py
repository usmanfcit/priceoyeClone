from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower
from django.views.generic import DetailView
from django_extensions.db.models import ActivatorModel

from .models import Product, Category, Vendor, ProductSpecificationCategory


class ProductDetailsView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "selected_product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_specification_categories"] = ProductSpecificationCategory.objects.filter(
            product=self.get_object())
        return context


class Homepage(ListView):
    model = Product
    template_name = "homepage.html"
    context_object_name = "products"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ProductListingByCategory(ListView):
    model = Product
    template_name = "category_product_page.html"
    paginate_by = 10

    def __init__(self):
        super().__init__()
        self.selected_category = None
        self.selected_vendors = None

    def get_queryset(self):
        self.selected_category = get_object_or_404(Category, name=self.kwargs["category_name"])
        self.selected_vendors = self.request.GET.getlist("vendor")
        queryset = Product.objects.filter(category=self.selected_category)
        if self.selected_vendors:
            queryset = queryset.filter(vendor__in=self.selected_vendors)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["vendors"] = (Vendor.objects.filter(product__category=self.selected_category)
                              .annotate(lower_name=Lower("name"))
                              .order_by("lower_name").distinct())
        context["selected_vendors"] = self.selected_vendors
        return context
