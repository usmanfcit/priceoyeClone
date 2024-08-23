from datetime import datetime, timezone
from django.core.mail import send_mail
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User, Role


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
        now = datetime.now(tz=timezone.utc)
        expires_in_minutes = (exp_time - now).total_seconds() / 60
        data.update({
            "expires_in_minutes": expires_in_minutes
        })
        return data


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "password", "email", "phone_number")

    def create(self, data):
        user = User.objects.create(
            phone_number=data["phone_number"],
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"]
        )
        user.set_password(data["password"])
        user.save()

        subject = "Welcome to Our Website!"
        plain_message = "Registered Successfully"
        from_email = 'stcoleridge88@gmail.com'
        to_email = user.email
        send_mail(subject, plain_message, from_email, [to_email])

        return user
