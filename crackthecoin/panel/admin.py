from django.contrib import admin
from .models import Jugador
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class JugadorInline(admin.StackedInline):
    model = Jugador
    can_delete = False
    verbose_name_plural = 'jugadores'

admin.site.register(Jugador)