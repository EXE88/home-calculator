from rest_framework import serializers
from django.contrib.auth.models import User

class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        
    username = serializers.CharField(max_length=50,min_length=5,required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)

class UserRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    username = serializers.CharField(max_length=50,min_length=5,required=True,allow_blank=False)
    email = serializers.EmailField(required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    confirm_password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    