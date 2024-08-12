from django.shortcuts import render, get_object_or_404, redirect

from orders.models import Order, OrderItem, SupportTicket
from products.models import Product


def add_to_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(
        user=current_user,
    )
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if not created:
        order_item.quantity += 1
        order_item.price = product.price * order_item.quantity
    else:
        order_item.price = product.price
    order_item.save()

    return redirect("orders:show_cart")


def delete_product_from_cart(request, product_id):
    item_to_delete = OrderItem.objects.get(product_id=product_id)
    item_to_delete.delete()
    return redirect("orders:show_cart")


def show_cart(request):
    order = Order.objects.get(user=request.user)
    return render(request, "show_cart.html", {"order": order})


def show_ticket_form(request, order_id):
    return render(request, "support_ticket_form.html", {"order_id": order_id})


def list_support_tickets(request):
    support_tickets = SupportTicket.objects.filter(user=request.user)
    return render(request, "list_support_tickets.html", {"support_tickets": support_tickets})


def create_support_ticket(request, order_id):
    user = request.user
    order = get_object_or_404(Order, id=order_id, user=user)

    subject = request.POST["subject"]
    description = request.POST["description"]

    support_ticket = SupportTicket.objects.get_or_create(user=user,
                                                         order=order,
                                                         title=subject,
                                                         description=description)
    return redirect("orders:list_support_tickets")
