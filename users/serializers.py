from rest_framework import serializers
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
    
    username = serializers.CharField(max_length=50,min_length=5,required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(self.context['request'],user)
            return user
        else:
            return serializers.ValidationError('invalid username or password')

class UserRegisterSerializers(serializers.ModelSerializer):   
    username = serializers.CharField(max_length=50,min_length=5,required=True,allow_blank=False)
    email = serializers.EmailField(required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    confirm_password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)