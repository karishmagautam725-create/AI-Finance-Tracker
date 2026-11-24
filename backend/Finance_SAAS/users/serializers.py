from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User=get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","email","password"]
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    password=serializers.CharField(write_only=True)
    email=serializers.EmailField()
    def validate(self, attrs):
        user=authenticate(
            email=attrs["email"],
            password=attrs["password"]
        )
        

        if not user:
            raise serializers.ValidationError("Invalid Credentials")
        refresh=RefreshToken.for_user(user)
        return{
            "user":user.email,
            "access":str(refresh.access_token),
            "refresh":str(refresh)
        }
    

        