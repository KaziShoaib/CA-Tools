from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path("", views.reports, name='reports'),
    path("login", views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path("ChangePassword", views.change_password_view, name="ChangePassword"),
    path("report/<int:report_id>", views.report, name="report"),
    path("submission", views.submission, name='submission'),
    path("CAList", views.CAList, name="CAList"),
    path("AddCA", views.AddCA, name="AddCA"),
    path("AddUser", views.AddUser, name="AddUser"),
    path("UserList", views.UserList, name="UserList"),
    path("ForgotPassword", views.forgot_password_view, name="ForgotPassword")
]
