import requests
from django.conf import settings
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class GoogleAuthView(APIView):

    def post(self, request):
        code = request.data.get("code")

        token_url = "https://oauth2.googleapis.com/token"

        token_data = {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": "http://localhost:8000/api/v1/users/google/",
            "grant_type": "authorization_code",
        }

        token_response = requests.post(token_url, data=token_data)
        token_json = token_response.json()

        access_token = token_json.get("access_token")

        user_info = requests.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers={"Authorization": f"Bearer {access_token}"}
        ).json()

        email = user_info.get("email")
        first_name = user_info.get("given_name")
        last_name = user_info.get("family_name")

        user, created = User.objects.get_or_create(email=email)

        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True
        user.registration_source = "google"
        user.last_login = timezone.now()
        user.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })