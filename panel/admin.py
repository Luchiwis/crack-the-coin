from django.contrib import admin
from .models import Jugador, Token
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class JugadorInline(admin.ModelAdmin):
    model = Jugador
    can_delete = False
    verbose_name_plural = 'jugadores'
    list_display = ['username', 'lock1', 'lock2', 'lock3', 'lock4', 'first_login', 'soulmate', 'winner', 'winned_date', 'saw_credits']

class TokenAdmin(admin.ModelAdmin):
    list_display = ['code', 'used', 'date_used', 'used_by']
    search_fields = ['code', 'used_by__username']
admin.site.register(Jugador, JugadorInline)
admin.site.register(Token, TokenAdmin)