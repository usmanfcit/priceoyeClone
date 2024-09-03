from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny

from products.models import Product, Vendor
from users.api.serializers import ReviewSerializer
from users.models import Review
from .filters import ProductFilter
from .serializers import ProductSerializer


class ProductReviewListingAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.get_active_reviews_for_model(Product, self.kwargs["object_id"])


class VendorReviewListingAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.get_active_reviews_for_model(Vendor, self.kwargs["object_id"])


class ProductListingAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        return Product.objects.active()
