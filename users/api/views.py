from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from orders.models import User
from .serializers import (
    UserSerializer,
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    UserProductReactionSerializer,
    UserProductReviewSerializer
)


class UserProductReviewAPIView(generics.CreateAPIView):
    serializer_class = UserProductReviewSerializer


class UserProductReactionAPIView(generics.CreateAPIView):
    serializer_class = UserProductReactionSerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserListing(generics.ListAPIView):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
