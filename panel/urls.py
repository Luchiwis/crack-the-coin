from django.urls import URLPattern, path, include
from . import views

urlpatterns = [path("", views.login, name="login"),
               path("accounts/", include("django.contrib.auth.urls")),
               path("login", views.login, name="login"),
               path("accounts/profile/", views.userpanel, name="userpanel"),
               path("userpanel", views.userpanel, name="userpanel"),
               path("lock1", views.lock1),
               path("lock2", views.lock2),
               path("lock3", views.lock3),
               path("lock4", views.lock4),
               path("credits", views.credits),
               ]
