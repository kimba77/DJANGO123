from django.urls import path
from . import views


urlpatterns = [
    path("registr/", views.RegisterView.as_view(), name="registartion_view"),
    path("login/", views.NewLoginView.as_view(), name="login_view"),
    path("users/", views.UserListView.as_view(), name="user_listView"),
]
