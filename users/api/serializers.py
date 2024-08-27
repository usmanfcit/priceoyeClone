from datetime import datetime, timezone

from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User, Role, UserProductReaction, Review
from .email import EmailService


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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserProductReaction
        fields = ("product", "reaction", "user")

    def create(self, data):
        user_product_reaction, created = UserProductReaction.objects.update_or_create(
            user=self.context["request"].user,
            product=data["product"],
            defaults={"reaction": data["reaction"]}
        )
        return user_product_reaction


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("content_type", "object_id", "review", "rating")

    def create(self, data):
        object_id = data["object_id"]
        content_type_id = data["content_type"].id
        review = data["review"]
        rating = data["rating"]
        user = self.context["request"].user

        content_type = ContentType.objects.get(pk=content_type_id)
        model_class = content_type.model_class()
        obj = model_class.objects.get(pk=object_id)
        object_name = obj.name

        review = Review.objects.create(
            content_type=content_type,
            object_id=object_id,
            object_name=object_name,
            user=user,
            review=review,
            rating=rating
        )
        return review
