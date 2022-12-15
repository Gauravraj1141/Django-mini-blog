from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.homepage),
    path("register", views.User_register, name="register"),
    path("login/", views.User_login, name="login"),
    path("profile/", views.User_profile, name="profile"),
    path("logout/", views.User_logout, name="logout"),

]
