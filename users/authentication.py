from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the user exists with the provided email or phone number
            user = User.objects.get(email=username) if '@' in username else User.objects.get(phone_number=username)
        except User.DoesNotExist:
            return None

        # If the user is found, check the password
        if user.check_password(password):
            return user
        return None


class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the user exists with the provided email or phone number
            user = User.objects.get(email=username) if '@' in username else User.objects.get(phone_number=username)
        except User.DoesNotExist:
            return None

        # If the user is found, check the password
        if user.check_password(password):
            return user
        return None