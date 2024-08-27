from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)

from products.models import Product
from .managers import UserManager
from .choices import RoleChoices, ReactionChoices


class Role(models.Model):
    name = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        unique=True,
        default=RoleChoices.CUSTOMER
    )

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


class UserProductReaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="user_reactions")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reactions")
    reaction = models.CharField(choices=ReactionChoices.choices, max_length=20, blank=True, null=True)
    date_reacted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name + " " + self.user.first_name + " " + self.reaction + " " + str(self.date_reacted)


class UserProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="user_reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    review = models.TextField()
    date_reviewed = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    def __str__(self):
        return self.product.name + " " + str(self.rating) + " " + self.user.email



