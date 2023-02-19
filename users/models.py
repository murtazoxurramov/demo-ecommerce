import uuid
from django.db import models
from django.contrib.auth.models import (AbstractUser, UserManager)
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

ORDINARY_USER, VENDOR, SUPER_USER = (
    "ordinary_user",
    "vendor",
    "super_user"
)


class BaseModel(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    _validate_phone = RegexValidator(
        regex=r"^9\d{12}$",
        message="Telefon raqamingiz 9 bilan boshlanishi va 12 belgidan oshmasligi kerak! Masalan: 998900459442"
    )
    USER_ROLES = (
        (ORDINARY_USER, ORDINARY_USER),
        (VENDOR, VENDOR),
        (SUPER_USER, SUPER_USER)
    )

    user_roles = models.CharField(
        max_length=31, choices=USER_ROLES, default=ORDINARY_USER
    )
    profile_image = models.ImageField(
        upload_to='upload/user', blank=True, null=True
    )
    phone_number = models.CharField(
        max_length=12, null=True, unique=True, validators=[_validate_phone]
    )
    email = models.EmailField(unique=True, blank=True, null=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
