from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
