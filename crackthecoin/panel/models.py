from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    lock1 = models.BooleanField(default=False)
    lock2 = models.BooleanField(default=False)
    lock3 = models.BooleanField(default=False)
    lock4 = models.BooleanField(default=False)

    first_login = models.DateTimeField(null=True, blank=True)
    soulmate = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    winner = models.BooleanField(default=False)
    winned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

class token_code(models.Model):
    code = models.CharField(max_length=100)
    used = models.BooleanField(default=False)
    date_used = models.DateTimeField(null=True, blank=True)
    used_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.code