from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProfileOwner


class UserRegisterApiView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = Users.objects.all()

class UserVerifyEmailApiView(generics.CreateAPIView):
    serializer_class = UserVerifyEmailSerializer
    queryset = Users.objects.all()


class UserLoginApiView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    queryset = Users.objects.all()


class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated , IsProfileOwner]
    queryset = Profile.objects.all()




    
