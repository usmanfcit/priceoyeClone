from rest_framework import generics, request
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from orders.models import User
from .serializers import UserSerializer, MyTokenObtainPairSerializer, RegisterSerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class AuthenticateUserView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class UserListing(AuthenticateUserView, generics.ListAPIView):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class UserDetail(AuthenticateUserView, generics.RetrieveAPIView):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class UserUpdate(AuthenticateUserView, generics.UpdateAPIView):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class UserDelete(AuthenticateUserView, generics.DestroyAPIView):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
