from django.contrib import admin

from orders.models import Order, OrderItem, SupportTicket

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(SupportTicket)
