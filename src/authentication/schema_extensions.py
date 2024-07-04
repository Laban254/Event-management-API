from drf_spectacular.utils import extend_schema_view, extend_schema
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework import status

user_registration_view_schema = extend_schema_view(
    post=extend_schema(
        summary="Register a new user",
        description="Create a new user account.",
        request=UserRegistrationSerializer,
        responses={
            status.HTTP_201_CREATED: 'User registered successfully',
            status.HTTP_400_BAD_REQUEST: 'Validation errors',
        }
    )
)

user_login_view_schema = extend_schema_view(
    post=extend_schema(
        summary="User login",
        description="Authenticate a user and return JWT tokens.",
        request=UserLoginSerializer,
        responses={
            status.HTTP_200_OK: {
                'type': 'object',
                'properties': {
                    'refresh': {'type': 'string', 'example': 'token_value'},
                    'access': {'type': 'string', 'example': 'token_value'},
                },
            },
            status.HTTP_400_BAD_REQUEST: 'Validation errors',
            status.HTTP_401_UNAUTHORIZED: 'Invalid credentials',
        }
    )
)