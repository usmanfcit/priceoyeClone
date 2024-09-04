from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User, Role, UserProductReaction, Review


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    model = User
    list_display = ["email"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "phone_number", "role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
        ("Profile Picture", {"fields": ("profile_picture",)})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "phone_number", "role", "password1", "password2"),
        }),
    )
    ordering = ("email",)


admin.site.register(Role)
admin.site.register(UserProductReaction)
admin.site.register(Review)
