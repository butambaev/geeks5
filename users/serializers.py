import random
from rest_framework import serializers
from django.conf import settings
from .models import ConfirmationCode

User = settings.AUTH_USER_MODEL 


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(required=False)  

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'password', 'phone_number')

    def create(self, validated_data):
        user = self.Meta.model.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number'),
            is_active=False
        )

        code = str(random.randint(100000, 999999))
        ConfirmationCode.objects.create(user=user, code=code)

        print(f"CONFIRMATION CODE: {code}")  

        return user


class ConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)