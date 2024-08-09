from django.shortcuts import render, redirect

from .status_choices import OrderStatusChoices
from orders.models import Order, OrderItem
from products.models import Product


def add_to_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(
        user=current_user,
        order_status=OrderStatusChoices.ORDER_RECEIVED,
    )
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if not created:
        order_item.quantity += 1
        order_item.price = product.price * order_item.quantity
    else:
        order_item.price = product.price
    order_item.save()

    order.total_price = 0
    for item in order.items.all():
        order.total_price += item.price
    order.save()

    return redirect("orders:show_cart")


def delete_product_from_cart(request, product_id):
    item_to_delete = OrderItem.objects.get(product_id=product_id)
    order = Order.objects.get()
    order.total_price = order.total_price - item_to_delete.price
    order.save()
    item_to_delete.delete()
    return redirect("orders:show_cart")


def show_cart(request):
    order = Order.objects.get(user=request.user)
    return render(request, "show_cart.html", {"order": order})
