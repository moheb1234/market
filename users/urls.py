from django.urls import path
from . import views

urlpatterns = [
    path('register' , views.UserRegisterApiView.as_view() , name = 'user-register'),
    path('verify-email/<int:verify_code>' , views.UserVerifyEmailApiView.as_view() , name = 'user-verify-email'),
    path('login' , views.UserLoginApiView.as_view() , name = 'user-login'),
    path('profile/<int:pk>' , views.ProfileApiView.as_view() , name = 'profile'),
    path('hire' , views.HireListCreateApiView.as_view() , name = 'hire'),
    path('support' , views.SupportListCreateApiView.as_view() , name = 'support'),
]