from rest_framework import status, viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
