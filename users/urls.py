from django.urls import path
from . import views

urlpatterns = [
    path('register' , views.UserRegisterApiView.as_view() , name = 'user-register'),
    path('verify-email/<int:verify_code>' , views.UserVerifyEmailApiView.as_view() , name = 'user-verify-email'),
    path('login' , views.UserLoginApiView.as_view() , name = 'user-login'),
    path('edit-personal-info' , views.UserPersonalInfoApiView.as_view() , name = 'user-edit-personal-info'),
]