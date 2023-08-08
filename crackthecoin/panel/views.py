from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from . import models
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/userpanel")
        else:
            return render(request, "registration/login.html", {"error": "Usuario o contraseña incorrectos"})
    else:
        print(request.user, "logged out")
        auth_logout(request)
        
    return render(request, "registration/login.html")

@login_required
def userpanel(request):
    user = request.user
    print(user.username, "logged in")
    ctx = {"user": user}
    return render(request, "userpanel.html", ctx)

@login_required
def lock1(request):
    if request.method == "POST":
        code = request.POST["code"]
        
    

    if not request.user.soulmate:
        # get first user sorted by last registration date
        request.user.soulmate = models.User.objects.order_by("registered")[0]
        print(request.user.soulmate.username, "is", request.user.username, "'s soulmate")

    ctx = {"user": request.user}
    return render(request, "lock1.html", ctx)

@login_required

def lock2(request):
    return render(request, "lock2.html")

@login_required

def lock3(request):
    return render(request, "lock3.html")

@login_required

def lock4(request):
    return render(request, "lock4.html")

@login_required
def credits(request):
    return render(request, "creditos.html")