from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status, permissions
from rest_framework.views import APIView
from oauth2_provider.models import get_application_model, get_grant_model
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.views.mixins import OAuthLibMixin
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from djoser.views import UserViewSet
from djoser import signals, utils
from djoser.compat import get_user_email
from djoser.conf import settings
from datetime import timedelta
from django.utils.timezone import localtime
import requests
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    user_logged_in,
    user_logged_out,
)
from rest_framework.exceptions import AuthenticationFailed

import json
from .serializers import CreateUserSerializer

from sso_config.settings_base import env


class UserRegister(OAuthLibMixin, APIView):
    permission_classes = (permissions.AllowAny,)

    def auto_authorize(self):
        """
        Automatically authorize on user registration for better user flow and get code
        """
        params = {}
        params["response_type"] = "code"
        params["code_challenge"] = env("CODE_CHALLENGE")
        params["code_challenge_method"] = "S256"
        params["client_id"] = env("CLIENT_ID")
        params["redirect_uri"] = "http://localhost:8000/noexist/callback"
        response = requests.get("http://localhost:8000/o/authorize/", params=params)

        return response

    def post(self, request):
        if self.request.auth is None:
            # data = self.request.data
            data = self.request.POST.dict()
            serializer = CreateUserSerializer(data=data)
            if serializer.is_valid():
                try:
                    with transaction.atomic():
                        user = serializer.save()
                        # Application = get_application_model()
                        # authorization_server = Application.objects.get(
                        #     client_id=env("CLIENT_ID")
                        # )
                        # Grant = get_grant_model()
                        # grant = Grant(
                        #     user=user,
                        #     application=authorization_server,
                        #     expires=localtime()
                        #     + timedelta(
                        #         seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS
                        #     ),
                        #     redirect_uri=authorization_server.redirect_uris,
                        #     code_challenge=env("CODE_CHALLENGE"),
                        #     code_challenge_method="S256",
                        #     scope="read write introspection",
                        # )
                        # grant.save()
                        # data["code"] = grant.code
                        # print(data)
                        # from OauthLibMixin
                        # data.pop("email")
                        # data.pop("first_name")
                        # data.pop("last_name")
                        # data.pop("password")
                        # data.pop("re_password")
                        # response = requests.post(
                        #     "http://localhost:8000/o/token/",
                        #     data,
                        #     headers={
                        #         "Content-Type": "application/x-www-form-urlencoded"
                        #     },
                        # )
                        # print(response.json(), "fgsfsgfgs")
                        # url, headers, body, token_status = self.create_token_response(
                        #     self.request
                        # )
                        # print(body)
                        # print(token_status)
                        # if token_status != 200:
                        #     raise Exception(
                        #         json.loads(body).get("error_description", "")
                        #     )
                        # djoser source perform_create
                        signals.user_registered.send(
                            sender=self.__class__, user=user, request=self.request
                        )
                        context = {"user": user}
                        to = [get_user_email(user)]
                        if settings.SEND_ACTIVATION_EMAIL:
                            settings.EMAIL.activation(self.request, context).send(to)
                        elif settings.SEND_CONFIRMATION_EMAIL:
                            settings.EMAIL.confirmation(self.request, context).send(to)
                        return Response(
                            {"message": "email sent"}, status=status.HTTP_201_CREATED
                        )
                except Exception as e:
                    return Response(
                        data={"error": e}, status=status.HTTP_400_BAD_REQUEST
                    )
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)


class UserLogin(OAuthLibMixin, APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data

        user = authenticate(request, email=data["email"], password=data["password"])
        if user is not None:
            login(request, user)
            # in Oauth2 flow upon login user should be redirected to /o/authorize/
            print(request.session.get_expiry_date())
            return Response(
                {"data": "User is now logged in"}, status=status.HTTP_200_OK
            )
        else:
            raise AuthenticationFailed("Invalid Credentials")

        # response = requests.post(
        #     "http://localhost:8000/o/token/",
        #     data,
        #     headers={"Content-Type": "application/x-www-form-urlencoded"},
        # )
        # return Response(response.json(), status=response.status_code)


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        logout(request)
        request.session.flush()
        print(request.session.get_expiry_date())
        return Response({"data": "User is now logged out"}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_stuff(request):
    return Response({"stuff": "stuff gotten"})
