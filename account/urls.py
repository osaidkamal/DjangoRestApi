from django.urls import path, include

from account.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, \
    SendPasswordResetEmailView, UserPasswordResetView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name='register'),
    path("login/", UserLoginView.as_view(), name='login'),
    path("profile/", UserProfileView.as_view(), name='profile'),
    path("changepass/", UserChangePasswordView.as_view(), name='changepass'),
    path("sent-reset-password-email/", SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

]
