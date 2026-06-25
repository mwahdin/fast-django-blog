from django.urls import path
from .views import SignUpView, LogInView, PasswordReset

app_name = 'account'

urlpatterns = [
    path('signup/',SignUpView.as_view(), name='signup'),
    path('login/',LogInView.as_view(), name='login'),
    path('password_reset/',PasswordReset.as_view(), name='password_reset'),
]
