from django.contrib import admin
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountInLine(admin.StackedInline):
    model = models.Account
    can_delete = False
    verbose_name_plural = "accounts"

class UserAdmin(admin.ModelAdmin):
    inlines = (AccountInLine, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)