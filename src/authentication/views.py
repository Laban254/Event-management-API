# views.py

from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import AllowAny
from .serializers import GenerateTokenSerializer

class GenerateTokenViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    serializer_class = GenerateTokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']

            User = get_user_model()
            try:
                user = User.objects.get(username=username)
                access_token = AccessToken.for_user(user)
                return Response({'access_token': str(access_token)}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': f'User with username {username} does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
