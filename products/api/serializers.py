from rest_framework import serializers

from products.models import Product, Category, Vendor


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
