from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views import generic
from .forms import RegisterationForm, LoginForm


class RegisterView(generic.CreateView):
    form_class = RegisterationForm
    template_name = "registation.html"
    success_url = "/bookshow/"


# Create your views here.


class NewLoginView(LoginView):
    form_class = LoginForm
    template_name = "login.html"
    success_url = "/bookshow/"

    # def get_success_url(self):
    #     return self.success_url

    def get_redirect_url(self):
        return self.success_url


class UserListView(generic.ListView):
    template_name = "users.html"
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset
