from django.urls import path
from .views import UserRegister, UserLogin, UserLogout, ReturnToken

urlpatterns = [
    # Override the default Djoser user creation URL
    path("users/", UserRegister.as_view(), name="custom-user-create"),
    path("login/", UserLogin.as_view(), name="custom-login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("token/", ReturnToken.as_view(), name="return-token"),
]
