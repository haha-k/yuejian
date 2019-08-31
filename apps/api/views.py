from django.shortcuts import render
from rest_framework_jwt.views import ObtainJSONWebToken
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.serializers import (
    JSONWebTokenSerializer
)
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework import status


jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER



class MyObtainJSONWebToken(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            print(".......")
            update_last_login(None, user)
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


obtain_jwt_token = MyObtainJSONWebToken.as_view()