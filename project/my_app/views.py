from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


def signin(request):
    login_error_message = None
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        myuser = authenticate(username=username, password=password)

        if myuser is not None:
            login(request, myuser)
            return render(request, "welcome.html", {"myuser": myuser})
        else:
            # return redirect("signup")
            login_error_message = "Wrong Account"

    return render(request, "signin.html", {"login_error_message": login_error_message})


# def signup(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password = request.POST["password"]

#         myuser = User.objects.create_user(username, email, password)
#         myuser.save()


#         return redirect("signin")
#     return render(request, "signup.html")
def signup(request):
    error_message = None
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            return redirect("signin")
        except IntegrityError:
            error_message = "User already exists"

    return render(request, "signup.html", {"error_message": error_message})


def signout(request):
    logout(request)
    return redirect("signin")
