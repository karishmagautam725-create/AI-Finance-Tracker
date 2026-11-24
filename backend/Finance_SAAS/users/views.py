from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView, Response
from .serializers import RegisterSerializer,LoginSerializer
from accounts.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes = [AllowAny]

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
    
class LogoutAPIVIEW(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        refresh_token=request.data["refresh"]
        token=RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message":"Loggedout Successfully"})
    
class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response(
            {
                "id":request.user.id,
                "email":request.user.email
            }
        )


