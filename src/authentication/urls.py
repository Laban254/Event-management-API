# urls.py
from django.urls import path, include
from rest_framework import routers
from .views import GenerateTokenViewSet

router = routers.DefaultRouter()
router.register(r'generate-token', GenerateTokenViewSet, basename='generate-token')

urlpatterns = [
    path('', include(router.urls)),
]
