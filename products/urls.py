from django.urls import path

from . import views

urlpatterns = [
    path("homepage/", views.homepage, name="homepage"),
    path('<str:category_name>/', views.category_product_page, name='category_products')
]

""" path("mobiles/", views.category_product_page, name="mobiles"),
    path("trimmers-shaver/", views.category_product_page, name="trimmers-shaver"),
    path("smart-watches/", views.category_product_page, name="smart-watches"),
    path("wireless-earbuds/", views.category_product_page, name="wireless-earbuds"),
    path("power-banks/", views.category_product_page, name="power-banks"),
    path("bluetooth-speakers/", views.category_product_page, name="bluetooth-speakers"),
    path("tablets/", views.category_product_page, name="tablets"),
    path("laptops/", views.category_product_page, name="laptops"),
    path("mobile-chargers/", views.category_product_page, name="mobile-chargers") """