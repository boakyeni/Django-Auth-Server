from django.urls import path
from .views import UserRegister, UserLogin, UserLogout, get_stuff

urlpatterns = [
    # Override the default Djoser user creation URL
    path("users/", UserRegister.as_view(), name="custom-user-create"),
    path("login/", UserLogin.as_view(), name="custom-login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("get-stuff", get_stuff, name="get_stuff"),
]
