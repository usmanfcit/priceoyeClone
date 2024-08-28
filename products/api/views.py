from django.contrib.contenttypes.models import ContentType
from rest_framework import generics
from rest_framework.permissions import AllowAny

from api.serializers import ProductSerializer
from products.models import Product, Vendor
from users.api.serializers import ReviewSerializer
from users.models import Review


class ProductReviewListingAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_content_type = ContentType.objects.get_for_model(Product)
        return Review.objects.filter(content_type=product_content_type, object_id=self.kwargs["object_id"])


class VendorReviewListingAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        vendor_content_type = ContentType.objects.get_for_model(Vendor)
        return Review.objects.filter(content_type=vendor_content_type, object_id=self.kwargs["object_id"])


class VendorProductListingAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(vendor__name=self.kwargs["vendor_name"])
