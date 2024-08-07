from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.shortcuts import render

from .models import Product, Category, Vendor, SpecificationCategory


def product_details(request, product_id, category_name):
    selected_product = Product.objects.get(id=product_id)
    product_specifications = selected_product.specifications.all()
    specification_categories = SpecificationCategory.objects.filter(details__product=selected_product).distinct()

    return render(request, "product_details.html", {
        "product_specifications": product_specifications,
        "selected_product": selected_product,
        "spec_categories": specification_categories
    })


def homepage(request):
    products = Product.objects.all()

    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(request, "homepage.html", {"page_object": page_object, "categories": categories})


def category_product_page(request, category_name):
    selected_category = Category.objects.get(name=category_name)
    category_products = Product.objects.filter(category=selected_category)

    selected_vendors = request.GET.getlist("vendor")
    if selected_vendors:
        vendor_filtered_products = category_products.filter(vendor__id__in=selected_vendors)
        paginator = Paginator(vendor_filtered_products, 12)
    else:
        paginator = Paginator(category_products, 12)

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
