from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.users.serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User(
            email=serializer.validated_data["email"],
            username=serializer.validated_data["email"],
        )
        user.set_password(serializer.validated_data["password"])
        user.save()
        return Response(status=status.HTTP_201_CREATED)