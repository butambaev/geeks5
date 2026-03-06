from django.urls import path
from .views import RegisterView, LoginView, ConfirmView
from .google_auth import GoogleAuthView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('confirm/', ConfirmView.as_view(), name='confirm'),
    path("google/", GoogleAuthView.as_view()),
]