from rest_framework import serializers

from orders.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
            "last_login",
            "date_joined",
            "role"
        )
