from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, "index.html")

def userpanel(request):
    return render(request, "userpanel.html")

def lock1(request):
    return render(request, "lock1.html")

def lock2(request):
    return render(request, "lock2.html")

def lock3(request):
    return render(request, "lock3.html")

def lock4(request):
    return render(request, "lock4.html")

def lock5(request):
    return render(request, "lock5.html")