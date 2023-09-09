from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserLoginSerializers,UserLoginValidateSerializer,UserRegisterSerializers,UserRegisterValidatePasswordSerializers

class UserLoginView(APIView):
    def post(self,request):
        login_serializer = UserLoginSerializers(data=request.data,context={"request":request})
        validate_serializer = UserLoginValidateSerializer(data=request.data,context={"request":request})
        if validate_serializer.is_valid():
            if login_serializer.is_valid():
                login_serializer.save()
                return Response('you are logedin successfully',status=status.HTTP_200_OK)
            else:
                return Response(login_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(validate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserRegisterView(APIView):
    def post(self,request):
        register_serializer = UserRegisterSerializers(data=request.data)
        validate_password_serializer = UserRegisterValidatePasswordSerializers(data=request.data,context={"request":request})
        if validate_password_serializer.is_valid() and register_serializer.is_valid():
            register_serializer.save()
            return Response('you are registered successfully',status=status.HTTP_200_OK)
        return Response(validate_password_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

