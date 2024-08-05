from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Product, Category


def homepage(request):
    products = Product.objects.all()

    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(request, "homepage.html", {"page_object": page_object, "categories": categories})


def category_product_page(request):
    path = request.path
    cleaned_path = path.strip("/")
    path_parts = cleaned_path.split("/")
    extracted_category_name = path_parts[-1]

    category_products = Category.objects.get(name=extracted_category_name)
    products = Product.objects.filter(category=category_products)

    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(request, "category_product_page.html", {"page_object": page_object, "categories": categories})
