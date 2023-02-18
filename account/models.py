from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, PermissionsMixin,
                                        UserManager)
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import UnicodeUsernameValidator

ORDINARY_USER, VENDOR, SUPER_USER = (
    "ordinary_user",
    "vendor",
    "super_user"
)


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password=password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    _validate_phone = RegexValidator(
        regex=r"^9\d{12}",
        message="Your phone number must start with 9 and not exceed 12 characters! For example: 998900459442"
    )
    _validate_username = UnicodeUsernameValidator()
    USER_ROLES = (
        (ORDINARY_USER, ORDINARY_USER),
        (VENDOR, VENDOR),
        (SUPER_USER, SUPER_USER)
    )

    user_roles = models.CharField(
        max_length=31, choices=USER_ROLES, default=ORDINARY_USER
    )
    username = models.CharField(
        _('username'), max_length=150, validators=[_validate_username], unique=True
    )
    phone_number = models.CharField(
        max_length=12, null=True, unique=True, validators=[_validate_phone]
    )
    email = models.EmailField(unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=150)
    profile_image = models.ImageField(
        upload_to='upload/user', blank=True, null=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        abstract = True

    # @property
    # def phone_number(self):
    #     return self.phone_number


class OrdinaryUser(CustomUser):
    class Meta:
        db_table = 'ordinary_user'
        verbose_name = 'Ordinary User'
        verbose_name_plural = 'Ordinary Users'

    def __str__(self):
        if self.full_name:
            return self.full_name
        else:
            return self.username


class Vendor(CustomUser):
    class Meta:
        db_table = 'vendor'
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __str__(self):
        if self.full_name:
            return self.full_name
        else:
            return self.username


class ShopCategory(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ar = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shop_category'
        verbose_name = 'Shop Category'
        verbose_name_plural = 'Shop Categories'

    def __str__(self):
        return self.title


class Shop(models.Model):
    name = models.CharField(max_length=255)
    ordinal_number = models.IntegerField(blank=True, null=True)
    logo = models.FileField(upload_to='upload/market', blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        Vendor, on_delete=models.SET_NULL, related_name='vendor', blank=True, null=True
    )
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shop'
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    def __str__(self):
        return self.name

    @property
    def logo_url(self):
        if self.logo:
            return "%s%s" % (settings.HOST, self.logo.url)
