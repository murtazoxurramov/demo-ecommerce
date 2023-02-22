from django.db import models

from users.models import User


class VendorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'vendor_profile'
        verbose_name = 'Vendor Profile'
        verbose_name_plural = 'Vendor Profiles'

    def __str__(self):
        return self.user.username

    # @property
    # def first_name(self):
    #     return self.user.first_name

    # @property
    # def last_name(self):
    #     return self.user.last_name

    # @property
    # def profile_image(self):
    #     return self.user.profile_image

    # @property
    # def phone_number(self):
    #     return self.user.phone_number

    # @property
    # def email(self):
    #     return self.user.email
