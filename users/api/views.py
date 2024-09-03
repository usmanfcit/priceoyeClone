from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User, UserProductReaction, Review
from .serializers import (
    UserSerializer,
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    UserProductReactionSerializer,
    ReviewSerializer
)


class ReviewAPIView(generics.CreateAPIView):
    serializer_class = ReviewSerializer


class UserProductReactionAPIView(generics.CreateAPIView):
    serializer_class = UserProductReactionSerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserListing(generics.ListAPIView):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class UserReactionListing(generics.ListAPIView):

    serializer_class = UserProductReactionSerializer

    def get_queryset(self):
        return UserProductReaction.objects.filter(user=self.request.user)


class UserReviewListing(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class ReactionUpdate(generics.UpdateAPIView):
    serializer_class = UserProductReactionSerializer

    def get_queryset(self):
        return UserProductReaction.objects.filter(user=self.request.user)


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class ReactionDelete(generics.DestroyAPIView):
    serializer_class = UserProductReactionSerializer

    def get_queryset(self):
        return UserProductReaction.objects.filter(user=self.request.user)


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
