from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    bank_account_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=100)
    max_daily_transfer_amount = models.FloatField(null=True)


class QrCode(models.Model):
    recipient = models.ForeignKey(User, models.CASCADE)
    amount = models.FloatField()
    date = models.DateTimeField()
    description = models.TextField()


class Wallet(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    balance = models.FloatField()


class Transaction(models.Model):
    sender = models.ForeignKey(User, models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(User, models.CASCADE, related_name='recipient')
    amount = models.FloatField()
    completed = models.BooleanField()
    date = models.DateTimeField()

