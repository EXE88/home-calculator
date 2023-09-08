from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserLoginSerializers,UserRegisterSerializers

class UserLoginView(APIView):
    def post(self,request):
        serializer = UserLoginSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('user logedin successfully',status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserRegisterView(APIView):
    def post(self,request):
        serializer = UserRegisterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('user created successfully',status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)