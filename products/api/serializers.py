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
    details = SpecificationDetailsSerializer(many=True)

    class Meta:
        model = ProductSpecificationCategory
        fields = ("specification_category", "details")


class ProductListingSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    vendor = VendorSerializer()
    specification_categories = ProductSpecificationCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ("name", "price", "image_url", "category", "vendor", "specification_categories")


class AddProductSerializer(serializers.ModelSerializer):
    specification_categories = ProductSpecificationCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ("name", "price", "image_url", "category", "vendor", "specification_categories")

    def create(self, validated_data):
        name = validated_data["name"]
        image_url = validated_data["image_url"]
        category = validated_data["category"]
        vendor = validated_data["vendor"]
        price = validated_data["price"]
        specification_categories = validated_data["specification_categories"]

        product = Product.objects.create(
            name=name,
            price=price,
            image_url=image_url,
            category=category,
            vendor=vendor,
        )
        for specification_category_detail in specification_categories:
            category_name = specification_category_detail["specification_category"]
            category_name = category_name["name"]
            specification_category, created = SpecificationCategory.objects.get_or_create(name=category_name)
            product_specification_category, created = ProductSpecificationCategory.objects.get_or_create(
                specification_category=specification_category,
                product=product
            )
            for specification_details in specification_category_detail["details"]:
                specification_label = specification_details["specification_label"]
                specification_value = specification_details["specification_value"]
                SpecificationDetail.objects.get_or_create(
                    specification_category=product_specification_category,
                    specification_label=specification_label,
                    specification_value=specification_value
                )
        return product
