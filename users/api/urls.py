from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.UserListing.as_view()),
    path("profile/<int:pk>/", views.UserDetail.as_view()),
    path("update/<int:pk>/", views.UserUpdate.as_view()),
    path("delete/<int:pk>/", views.UserDelete.as_view()),
    path("login/", views.LoginView.as_view()),
    path("register/", views.UserRegistrationAPIView.as_view()),
    path("react-to-product/", views.UserProductReactionAPIView.as_view()),
    path("create-review/", views.ReviewAPIView.as_view()),
    path("react-to-product/delete/<int:pk>/", views.ReactionDelete.as_view()),
    path("react-to-product/update/<int:pk>/", views.ReactionUpdate.as_view()),
    path("react-to-product/list/", views.UserReactionListing.as_view()),
    path("review-for-product/list/", views.UserReviewListing.as_view()),
]
