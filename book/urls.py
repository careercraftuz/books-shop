from django.contrib import admin
from django.urls import path
from.views import(
    Users,
    UserView,
)

urlpatterns = [
     path('users/<int:id>', UserView.as_view()),
    path('users/', Users.as_view()),    ]