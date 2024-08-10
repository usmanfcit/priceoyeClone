from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django_extensions.db.models import ActivatorModel

from .models import Product, Category, Vendor, ProductSpecificationCategory


def product_detail(request, product_id, category_name):
    selected_product = get_object_or_404(Product, id=product_id, status=ActivatorModel.ACTIVE_STATUS)
    spec_groups = ProductSpecificationCategory.objects.filter(product=selected_product)

    return render(request, "product_detail.html", {
        "selected_product": selected_product,
        "spec_groups": spec_groups,
    })


def homepage(request):
    products = Product.objects.all()

    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(request, "homepage.html", {"page_object": page_object, "categories": categories})


def product_listing_by_category(request, category_name):
    selected_category = get_object_or_404(Category, name=category_name)
    selected_vendors = request.GET.getlist("vendor")

    if selected_vendors:
        products = Product.objects.filter(category=selected_category, vendor__id__in=selected_vendors)
        paginator = Paginator(products, 12)
    else:
        products = Product.objects.filter(category=selected_category)
        paginator = Paginator(products, 12)

    page_number = request.GET.get("page")
    paginated_products_object = paginator.get_page(page_number)

    categories = Category.objects.all()
    vendors = (Vendor.objects.filter(product__category=selected_category)
               .annotate(lower_name=Lower("name"))
               .order_by("lower_name").distinct())

    return render(request, "category_product_page.html", {
        "page_object": paginated_products_object,
        "categories": categories,
        "vendors": vendors,
        "selected_vendors": selected_vendors
    })
