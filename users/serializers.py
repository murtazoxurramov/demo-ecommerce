from rest_framework import serializers
from .models import User

from .authentication import EmailOrPhoneBackend

class EmailOrPhoneTokenObtainPairSerializer(serializers.Serializer):
    email_or_phone = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    def validate(self, attrs):
        email_or_phone = attrs.get('email_or_phone')
        password = attrs.get('password')

        if email_or_phone and password:
            user = EmailOrPhoneBackend().authenticate(request=self.context.get('request'), username=email_or_phone, password=password)
            if not user:
                raise serializers.ValidationError('Invalid email/phone number or password')
        else:
            raise serializers.ValidationError('Must include "email_or_phone" and "password"')

        attrs['user'] = user
        return attrs


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'profile_image', 'phone_number', 'email']
