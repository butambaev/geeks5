from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)

    birthdate = models.DateField(null=True, blank=True)

    registration_source = models.CharField(
        max_length=50,
        default="local",
        blank=True,
        null=True
    )

    last_login = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]

    def __str__(self):
        return self.email


class ConfirmationCode(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='confirmation'
    )
    code = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.user.email} - {self.code}"