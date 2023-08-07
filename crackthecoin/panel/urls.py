from django.urls import URLPattern, path
from . import views

urlpatterns = [path("", views.index),
               path("userpanel", views.userpanel),
               path("lock1", views.lock1),
               path("lock2", views.lock2),
               path("lock3", views.lock3),
               path("lock4", views.lock4),
               path("lock5", views.lock5),
               ]
