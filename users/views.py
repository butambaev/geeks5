from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import ConfirmationCode
from .serializers import (
    RegisterSerializer,
    ConfirmSerializer,
    LoginSerializer
)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "User registered. Check confirmation code."},
            status=status.HTTP_201_CREATED
        )


class ConfirmView(APIView):
    def post(self, request):
        serializer = ConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        code = serializer.validated_data['code']

        try:
            user = User.objects.get(username=username)
            confirmation = user.confirmation
        except:
            return Response({"error": "Invalid user"}, status=400)

        if confirmation.code != code:
            return Response({"error": "Invalid code"}, status=400)

        user.is_active = True
        user.save()
        confirmation.delete()

        return Response({"message": "User confirmed successfully"})


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response({"error": "Invalid credentials"}, status=400)

        if not user.is_active:
            return Response({"error": "User is not confirmed"}, status=403)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})
