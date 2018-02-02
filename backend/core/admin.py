from django.contrib import admin

# Register your models here.
from core.models import QrCode, Wallet, Transaction, UserProfile

admin.site.register(UserProfile)
admin.site.register(QrCode)
admin.site.register(Wallet)
admin.site.register(Transaction)