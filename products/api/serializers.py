from rest_framework import serializers

from products.models import Product, Category, Vendor, ProductSpecificationCategory, SpecificationDetail, \
    SpecificationCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    vendor = VendorSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class SpecificationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationCategory
        fields = ("name",)


class SpecificationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationDetail
        fields = "__all__"


class ProductSpecificationCategorySerializer(serializers.ModelSerializer):
    specification_category = SpecificationCategorySerializer()
    details = SpecificationDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = ProductSpecificationCategory
        fields = ("specification_category", "details")


class ProductListingSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    vendor = VendorSerializer()
    specification_categories = ProductSpecificationCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ("name", "price", "image_url", "category", "vendor", "specification_categories")


class AddProductSerializer(serializers.ModelSerializer):
    specification_categories = ProductSpecificationCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ("name", "price", "image_url", "category", "vendor", "specification_categories")
