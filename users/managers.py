from django.apps import apps
from django.contrib.auth.models import BaseUserManager
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import ActivatorModel

from .choices import RoleChoices


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)
        role = extra_fields.pop("role", None)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        Role = apps.get_model("users", "Role")
        role, created = Role.objects.get_or_create(name=RoleChoices.ADMIN)
        return self._create_user(email, password, role=role, **extra_fields)

    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)


class ReviewManager(models.Manager):
    def active(self):
        return self.filter(status=ActivatorModel.ACTIVE_STATUS)

    def inactive(self):
        return self.filter(status=ActivatorModel.INACTIVE_STATUS)

    def get_active_reviews_for_model(self, model, object_id):
        content_type = ContentType.objects.get_for_model(model)
        return self.filter(content_type=content_type, object_id=object_id, status=ActivatorModel.ACTIVE_STATUS)
