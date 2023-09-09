from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

class UserLoginValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']
      
    email = serializers.EmailField(required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    
    def validate(self, attrs):
        request = self.context['request']
        email = attrs.get("email")
        password = attrs.get("password")
        user = User.objects.filter(email=email)
        username = user[0].username
        user = authenticate(request=request,username=username,password=password)
        if user is not None:
            return user
        raise serializers.ValidationError('email or password is wrong')

class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']
      
    email = serializers.EmailField(required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    
    def create(self, validated_data):
        request = self.context['request']
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = User.objects.filter(email=email)
        username = user[0].username
        user = authenticate(request=request,username=username,password=password)
        login(request,user)
        return user
    
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
        