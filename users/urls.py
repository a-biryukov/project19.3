from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, RecoveryTemplateView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(http_method_names=["post", "get", "options"], template_name="users/logout.html"), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email_confirm"),
    path("password-recovery/", RecoveryTemplateView.as_view(), name="password_recovery"),
    path("change/<int:pk>", UserUpdateView.as_view(), name="change")
]
