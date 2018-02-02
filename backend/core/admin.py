from django.contrib import admin

# Register your models here.
from core.models import User, QrCode, Wallet, Transaction

admin.site.register(User)
admin.site.register(QrCode)
admin.site.register(Wallet)
admin.site.register(Transaction)
