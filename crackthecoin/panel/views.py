from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from . import models
from django.utils import timezone
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # first login check
            if user.jugador.first_login is None:
                user.jugador.first_login = timezone.now()
                user.jugador.save()
                print("first logged in:", user.username, user.jugador.first_login)
            else:
                print("logged in:", user.username)
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
    print(user.username, "showing pannel for:", request.user.username)
    # set soulmate to the last user who logged in
    if user.jugador.soulmate is None:
        user.jugador.soulmate = models.Jugador.objects.filter(winner=False).order_by("-first_login")[1]
        user.jugador.save()
        print("soulmate of ", user.username ," set to:", user.jugador.soulmate.username)
    ctx = {"user": user}
    return render(request, "userpanel.html", ctx)

@login_required
def lock1(request):
    if request.method == "POST":
        code = request.POST["code"]
        
    
    print("showing lock1 for:", request.user.username)

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