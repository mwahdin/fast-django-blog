from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


# Create your views here.
User = get_user_model()

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/page-login.html'
    success_url = reverse_lazy('account:login')

class LogInView(LoginView):
    pass