from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView

from orders.models import Order, OrderItem, SupportTicket
from products.models import Product
from .status_choices import OrderStatusChoices


class FinalizeOrder(View):
    def post(self, request, *args, **kwargs):
        order_id = kwargs["order_id"]
        Order.objects.filter(id=order_id).update(
            order_status=OrderStatusChoices.ORDER_PLACED
        )
        return redirect("orders:show_orders")


class AddToCart(View):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        product_id = self.kwargs["product_id"]
        product = Product.objects.get(id=product_id)
        order, created = Order.objects.get_or_create(
            user=current_user,
            order_status=OrderStatusChoices.IN_CART
        )
        order_item, order_item_created = OrderItem.objects.get_or_create(order=order, product=product)

        if not order_item_created:
            OrderItem.objects.filter(order=order, product=product).update(
                quantity=F("quantity") + 1,
                price=F("price") + product.price
            )
        else:
            OrderItem.objects.filter(order=order, product=product).update(
                price=product.price
            )

        return redirect("orders:show_cart")


class DeleteProductFromCart(DeleteView):
    model = OrderItem
    template_name = "orderitem_confirm_delete.html"
    success_url = reverse_lazy("orders:show_cart")


class ShowOrders(ListView):
    model = Order
    template_name = "show_orders.html"
    context_object_name = "orders"

    def get_queryset(self, queryset=None):
        return Order.objects.filter(user=self.request.user, order_status=OrderStatusChoices.ORDER_PLACED)


class ShowCart(DetailView):
    model = Order
    template_name = "show_cart.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        order = get_object_or_404(Order, user=self.request.user, order_status=OrderStatusChoices.IN_CART)
        return order


class ShowTicketForm(DetailView):
    model = Order
    template_name = "support_ticket_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_id"] = self.kwargs["pk"]
        return context


class ListSupportTickets(ListView):
    model = SupportTicket
    template_name = "list_support_tickets.html"
    context_object_name = "support_tickets"

    def get_queryset(self):
        support_tickets = SupportTicket.objects.filter(user=self.request.user)
        return support_tickets


class CreateSupportTicket(CreateView):
    model = SupportTicket
    template_name = "support_ticket_form.html"

    def post(self, request, *args, **kwargs):
        order_id = self.kwargs["order_id"]
        user = request.user
        order = get_object_or_404(Order, id=order_id, user=user)
        subject = request.POST["subject"]
        description = request.POST["description"]

        SupportTicket.objects.get_or_create(user=user,
                                            order=order,
                                            title=subject,
                                            description=description)

        return redirect("orders:list_support_tickets")
