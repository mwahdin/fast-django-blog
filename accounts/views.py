from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


# Create your views here.
User = get_user_model()

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('account:login')

class LogInView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomLoginForm
    success_url = reverse_lazy('websit')

class PasswordReset():
    pass