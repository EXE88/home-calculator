from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserLoginSerializers,UserRegisterSerializers,UserRegisterValidatePasswordSerializers

class UserLoginView(APIView):
    def post(self,request):
        serializer = UserLoginSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('user logedin',status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserRegisterView(APIView):
    def post(self,request):
        register_serializer = UserRegisterSerializers(data=request.data)
        validate_password_serializer = UserRegisterValidatePasswordSerializers(data=request.data,context={"request":request})
        if validate_password_serializer.is_valid() and register_serializer.is_valid():
            register_serializer.save()
            return Response('user created',status=status.HTTP_200_OK)
        return Response(validate_password_serializer.errors,status=status.HTTP_400_BAD_REQUEST)