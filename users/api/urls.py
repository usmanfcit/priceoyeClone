from django.urls import path
from . import views

urlpatterns = [
    path("users", views.UserListing.as_view()),
    path("user/profile/<int:pk>", views.UserDetail.as_view()),
    path("user/update/<int:pk>", views.UserUpdate.as_view()),
    path("user/delete/<int:pk>", views.UserDelete.as_view()),
    path("user/login", views.LoginView.as_view()),
    path("user/register", views.UserRegistrationAPIView.as_view()),
    path("user/react-to-product/<str:action>", views.UserProductReactionAPIView.as_view()),
    path("user/review-for-product", views.UserProductReviewAPIView.as_view())
]
