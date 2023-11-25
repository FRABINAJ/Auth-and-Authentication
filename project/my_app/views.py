from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, "index.html")


def signup(request):
    user_already_exist = None
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            myuser = User.objects.create_user(name, email, password)
            myuser.save()
            return redirect("signin")
        except IntegrityError:
            user_already_exist = "User already exist"

    return render(request, "signup.html", {"user_already_exist": user_already_exist})


def signin(request):
    login_error = None
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]

        myuser = authenticate(username=name, password=password)
        if myuser is not None:
            login(request, myuser)
            return render(request, "welcome.html", {"myuser": myuser})
        else:
            login_error = "Login error"

    return render(request, "signin.html", {"login_error": login_error})


def signout(request):
    logout(request)
    return redirect("sihnin")
