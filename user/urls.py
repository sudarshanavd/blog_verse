from django.urls import path
from .views import SignUpView
from django.contrib.auth import views

urlpatterns = [
path('signup/', SignUpView.as_view(), name='signup'),
path("login/", views.LoginView.as_view(template_name='user/login.html'), name="login"),
path("logout/", views.LogoutView.as_view(), name="logout"),
path("password_change/",views.PasswordChangeView.as_view(template_name='user/password_change_form.html'),name="password_change"),
path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordResetView.as_view(template_name='user/password_reset_form.html'), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
        name="password_reset_complete",
    ),
]