from rest_framework import generics
from .models import Users
from .serializers import *
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated


class UserRegisterApiView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = Users.objects.all()

class UserVerifyEmailApiView(generics.UpdateAPIView):
    serializer_class = UserVerifyEmailSerializer
    queryset = Users.objects.all()

    def get_object(self):
        verify_code =  self.request.data['verify_code']
        try:
            user =  Users.objects.get(verify_code = verify_code)
            return user
        except ObjectDoesNotExist:
            raise  ValidationError(detail={'detail':'verify code is invalid'})


class UserLoginApiView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    queryset = Users.objects.all()


class UserPersonalInfoApiView(generics.RetrieveUpdateAPIView):
    serializer_class = UserEditPersonalInfoSerializer
    permission_classes = [IsAuthenticated]
    queryset = Users.objects.all()

    def get_object(self):
        return self.request.user
    


    
