from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# user register

class User_register_form(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "password"}), label="Password (Re-enter)")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]
        labels = {"email": "Email"}


# User login form

class User_login_form(AuthenticationForm):
    pass
