import django_filters
from orders.models import Order


class OrderFilter(django_filters.FilterSet):
    created_after = django_filters.DateFilter(field_name="created", lookup_expr="gte")
    created_before = django_filters.DateFilter(field_name="created", lookup_expr="lte")

    class Meta:
        model = Order
        fields = ["order_status", "created_after", "created_before"]
