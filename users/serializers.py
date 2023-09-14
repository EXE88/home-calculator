from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

class UserLoginValidateSerializer(serializers.Serializer):
    email_or_username = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    
    def validate(self, attrs):
        request = self.context['request']
        email_or_username = attrs.get("email_or_username")
        password = attrs.get("password")
        if '@gmail.com' in email_or_username or '@' in email_or_username and '.com' in email_or_username:
            user = User.objects.filter(email=email_or_username)
            try:
                username = user[0].username
            except:
                raise serializers.ValidationError('email or password is wrong')
            user_auth = authenticate(request=request,username=username,password=password)
            if user_auth is not None:
                return user_auth
            raise serializers.ValidationError('email or password is wrong')
        user_auth = authenticate(request=request,username=email_or_username,password=password)
        if user_auth is not None:
            return user_auth
        raise serializers.ValidationError('username or password is wrong')
    
class UserLoginSerializers(serializers.Serializer):
    email_or_username = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    
    def create(self, validated_data):
        request = self.context['request']
        email_or_username = validated_data.get("email_or_username")
        password = validated_data.get("password")
        if '@gmail.com' in email_or_username or '@' in email_or_username and '.com' in email_or_username:
            user = User.objects.filter(email=email_or_username)
            username = user[0].username
            user_auth = authenticate(request=request,username=username,password=password)
            login(request,user_auth)
            return user_auth
        user_auth = authenticate(request=request,username=email_or_username,password=password)
        login(request,user_auth)
        return user_auth
    
class UserRegisterValidatePasswordSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=50,min_length=5,required=True,allow_blank=False)
    email = serializers.EmailField(required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    confirm_password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    
    def validate(self, attrs):
        username = attrs.get("username")
        email = attrs.get("email")
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        
        username_validateing = User.objects.filter(username=username).exists()
        email_validateing = User.objects.filter(email=email).exists()
        
        if username_validateing:
            raise serializers.ValidationError('there is a user with this username')
        
        if email_validateing:
            raise serializers.ValidationError('there is a user whith this email')
        
        if password != confirm_password:
            raise serializers.ValidationError('passwords is not match')
        return username

class UserRegisterSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=50,min_length=5,required=True,allow_blank=False)
    email = serializers.EmailField(required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)    
    
    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        new_user = User.objects.create_user(username=username,email=email,password=password)
        return new_user
        