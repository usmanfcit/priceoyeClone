from datetime import datetime, timezone

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User, Role, UserProductReaction, UserProductReview
from products.models import Product, Category, Vendor
from .email import EmailService


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    vendor = VendorSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "is_active",
            "date_joined",
            "last_login",
            "role"
        ]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        exp_timestamp = self.get_token(self.user)["exp"]
        exp_time = datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)
        expiry_time = exp_time.isoformat()
        user_data_serialized = UserSerializer(self.user)
        user_data = user_data_serialized.data
        user_data["exp"] = expiry_time
        user_data["access"] = data["access"]
        user_data["refresh"] = data["refresh"]
        return user_data


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "password", "email", "phone_number")

    def create(self, data):
        user = super().create(data)
        user.set_password(data["password"])
        user.save()
        email_service = EmailService()
        email_service.send_registration_email(user)
        return user


class UserProductReactionSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


class UserProductReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProductReaction
        fields = ("product",)

    def create(self, data):
        product = data["product"]
        user = self.context["request"].user
        reaction = self.context["request"].parser_context["kwargs"]["action"]
        user_product_reaction, created = UserProductReaction.objects.update_or_create(
            user=user,
            product=product,
            defaults={"reaction": reaction}
        )
        return user_product_reaction


class UserProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProductReview
        fields = ("product", "review", "rating")

    def create(self, data):
        product = data["product"]
        review = data["review"]
        rating = data["rating"]
        user = self.context["request"].user

        user_product_review, created = UserProductReview.objects.update_or_create(
            user=user,
            product=product,
            defaults={"review": review, "rating": rating}
        )
        return user_product_review
