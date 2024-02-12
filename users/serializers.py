from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import Users
from rest_framework.exceptions import  AuthenticationFailed , PermissionDenied , NotFound
from .email import send_verify_code
from .exceptions import Server_Error
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import AccessToken
import random


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True , max_length = 32)
    message = serializers.CharField(read_only=True)
    class Meta:
        model = Users
        fields = ['username' , 'email' , 'password' , 'confirm_password' , 'message']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self , validated_data):
        del validated_data['confirm_password']
        user =  Users.objects.create(**validated_data)
        user.is_active=False
        user.verify_code = random.randint(100000,999999)
        user.save()
        try:
            send_verify_code(email= user.email , verify_code= user.verify_code , username= user.username)
        except Exception:
            user.delete()
            raise Server_Error()
        validated_data['message'] = f'Registration was successful we send a verify code to {user.email} . please check your email'
        return validated_data

    def validate(self , attrs):
        if not check_password(attrs['confirm_password'] , attrs['password']):
            raise serializers.ValidationError('password dose not match')
        return attrs
    
    def validate_password(self, value):
        return make_password(value)

    
class UserVerifyEmailSerializer(serializers.Serializer):

    def create(self , validated_data):
        verify_code = self.context['view'].kwargs['verify_code']
        try:
            user = Users.objects.get(verify_code= verify_code)
            user.is_active = True
            user.verify_code = None
            user.save()
            return validated_data
        except ObjectDoesNotExist:
            raise serializers.ValidationError(detail= {'details' : 'verify code is invalid'})


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True )
    password = serializers.CharField(write_only=True )
    token = serializers.CharField(read_only=True )

    def create(self , validated_data):
        try:
            user = Users.objects.get(username= validated_data['username'])
            if not check_password(validated_data['password'] , user.password):
                raise AuthenticationFailed(detail={'details':'password is wrong'})
            token = AccessToken.for_user(user)
            if not user.is_active:
                raise PermissionDenied(detail={'details':'you need to verify your email'})
            validated_data['token'] = token
            return validated_data
        except ObjectDoesNotExist:
            raise NotFound(detail= {'details':'no user founded'})



class UserEditPersonalInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['phone_number','passport_number','card','photo','birthday','country','city' ]

    def update(self , instance , validated_data):
        Users.objects.filter(pk = instance.id).update(**validated_data)
        return validated_data


        
        