from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
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

class PasswordReset(PasswordResetView):
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('account:password_reset_done')
    email_template_name = 'registration/password_reset_email.html'

class PasswordResetDone(PasswordResetDoneView):
    template_name ='registration/password_reset_done.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'