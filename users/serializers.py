from rest_framework import serializers
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

class UserLoginValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
      
=======
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
    
>>>>>>> master
    username = serializers.CharField(max_length=50,min_length=5,required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    
    def validate(self, attrs):
        request = self.context['request']
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            return user
        raise serializers.ValidationError('username or password is wrong')

<<<<<<< HEAD
class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
      
    username = serializers.CharField(max_length=50,min_length=5,required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    
    def create(self, validated_data):
        request = self.context['request']
        username = validated_data.get("username")
        password = validated_data.get("password")
        user = authenticate(request,username=username,password=password)
        login(request,user)
        return user
    
class UserRegisterValidatePasswordSerializers(serializers.Serializer):
=======
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
    class Meta:
        model=User
        fields = '__all__'
        
>>>>>>> master
    username = serializers.CharField(max_length=50,min_length=5,required=True,allow_blank=False)
    email = serializers.EmailField(required=True,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    confirm_password = serializers.CharField(max_length=50,min_length=8,required=True,allow_blank=False)
    
    def validate(self, attrs):
        username = attrs.get("username")
        email = attrs.get("email")
<<<<<<< HEAD
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
        
=======
        first_password = attrs.get("password")
        secend_password = attrs.get("confirm_password")
        
        user = authenticate(username=username,email=email)
        
        if user is not None:
            return serializers.ValidationError('There is a user with this email and username')
        if first_password == secend_password:
            return attrs
        return serializers.ValidationError('passwords is diffrend from eachother')
    
    def create(self, validated_data):
        username = validated_data.get("username")
        email = validated_data.get("email")
        password = validated_data.get("password")
        
        new_user = User.objects.create_user(username=username,email=email,password=password)
        return new_user
>>>>>>> master
