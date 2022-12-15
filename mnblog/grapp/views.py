from django.shortcuts import render, redirect
from .forms import User_register_form, User_login_form
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


# homepage

def homepage(request):
    if request.user.is_authenticated:
        login = True
        return render(request, "blogapp/home.html", {"login": login})
    else:
        login = False
        return render(request, "blogapp/home.html", {"login": login})


# user register

def User_register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fmdata = User_register_form(request.POST)
            if fmdata.is_valid():
                fmdata.save()
                messages.success(request, 'User have been registered')
        else:
            fmdata = User_register_form()
        return render(request, "blogapp/register.html", {"form": fmdata})
    else:
        return redirect("/profile/")


# user login

def User_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fmdata = User_login_form(request=request, data=request.POST)
            if fmdata.is_valid():
                uname = fmdata.cleaned_data["username"]
                psw = fmdata.cleaned_data["password"]
                realuser = authenticate(username=uname, password=psw)
                if realuser is not None:
                    login(request, realuser)
                    messages.success(request, "login successfully")
                    return redirect("/profile/")
        else:
            fmdata = User_login_form(request=request)

        return render(request, "blogapp/login.html", {"form": fmdata})
    else:
        return redirect("/profile/")


# user logout


def User_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")
    else:
        return redirect("register")


# User Profile

def User_profile(request):
    if request.user.is_authenticated:

        return render(request, "blogapp/profile.html", {"name": request.user})
    else:
        return redirect("/")
