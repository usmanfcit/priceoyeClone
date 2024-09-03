from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from products.models import Product, Vendor, Category
from users.api.serializers import ReviewSerializer
from users.models import Review
from .filters import ProductFilter
from .permissions import IsStaff
from .serializers import AddProductSerializer, VendorSerializer, CategorySerializer, \
    ProductListingSerializer


class AllowAnyPermissionMixin:
    permission_classes = (AllowAny,)


class ProductReviewListingAPIView(AllowAnyPermissionMixin, generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.get_active_reviews_for_model(Product, self.kwargs["object_id"])


class VendorReviewListingAPIView(AllowAnyPermissionMixin, generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.get_active_reviews_for_model(Vendor, self.kwargs["object_id"])


class ProductListingAPIView(AllowAnyPermissionMixin, generics.ListAPIView):
    serializer_class = ProductListingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        return Product.objects.active()


class StaffPermissionMixin:
    permission_classes = (IsStaff, IsAuthenticated)


class AddProductAPIView(StaffPermissionMixin, generics.CreateAPIView):
    serializer_class = AddProductSerializer


class UpdateProductAPIView(StaffPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer


class DeleteProductAPIView(StaffPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer


class AddVendorAPIView(StaffPermissionMixin, generics.CreateAPIView):
    serializer_class = VendorSerializer


class UpdateVendorAPIView(StaffPermissionMixin, generics.UpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class DeleteVendorAPIView(StaffPermissionMixin, generics.DestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class AddCategoryAPIView(StaffPermissionMixin, generics.CreateAPIView):
    serializer_class = CategorySerializer


class UpdateCategoryAPIView(StaffPermissionMixin, generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeleteCategoryAPIView(StaffPermissionMixin, generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
