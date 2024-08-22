from django.urls import path
from . import views

urlpatterns = [
    path('users', views.UserListing.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('users/update/<int:pk>', views.UserUpdate.as_view()),
    path('users/delete/<int:pk>', views.UserDelete.as_view()),
    path('users/create', views.UserCreate.as_view())

]
