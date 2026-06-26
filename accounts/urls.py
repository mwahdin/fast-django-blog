from django.urls import path
from .views import SignUpView, LogInView, PasswordReset, PasswordResetDone, PasswordResetConfirm, PasswordResetComplete

app_name = 'account'

urlpatterns = [
    path('signup/',SignUpView.as_view(), name='signup'),
    path('login/',LogInView.as_view(), name='login'),
    path('password-reset/', PasswordReset.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),
]
