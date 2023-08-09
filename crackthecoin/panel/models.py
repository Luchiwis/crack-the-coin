from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.

class Jugador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

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

class Token(models.Model):
    code = models.CharField(max_length=100)
    used = models.BooleanField(default=False)
    date_used = models.DateTimeField(null=True, blank=True)
    used_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.code
    

# create jugador when user is created
@receiver(models.signals.post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Jugador.objects.create(user=instance, username=instance.username, password=instance.password)