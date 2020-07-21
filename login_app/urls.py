from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logoutUser, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('register/', views.createUser, name='register'),

    # Reset password
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name='login_app/reset_password.html'), name="reset_password"),
    path("reset_password/sent/", auth_views.PasswordResetDoneView.as_view(template_name='login_app/email_sent.html'), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='login_app/set-password.html'), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='login_app/reset_complete.html'), name="password_reset_complete"),
]