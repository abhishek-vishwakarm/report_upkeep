from django.urls import path
from my_app.views import UserLoginView, UserRegistrationView, UserProfileView, SendPasswordResetEmailView, UserPasswordResetView
urlpatterns = [
    path('register', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name='reset-password'),

]
