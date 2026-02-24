from django.urls import path
from .views import RegisterView, LoginView, ConfirmView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('confirm/', ConfirmView.as_view(), name='confirm'),
]