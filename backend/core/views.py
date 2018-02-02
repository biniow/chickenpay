from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from core.models import User, QrCode, Wallet, Transaction
from core.serializers import UserSerializer, QrCodeSerializer, WalletSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QrCodeList(generics.ListCreateAPIView):
    queryset = QrCode.objects.all()
    serializer_class = QrCodeSerializer


class QrCodeDetail(generics.RetrieveAPIView):
    queryset = QrCode.objects.all()
    serializer_class = QrCodeSerializer


class WalletList(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletDetail(generics.RetrieveUpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = Transaction


class TransactionDetail(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = Transaction


