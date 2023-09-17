from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions

class UpdatePrices(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        pass