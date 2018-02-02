from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

from core.models import QrCode, Wallet, Transaction, UserProfile
from core.permissions import IsAdminUser, IsUserOwner
from core.serializers import UserProfileSerializer, QrCodeSerializer, WalletSerializer, UserSerializer, \
    RegistrationSerializer


class UserList(generics.ListAPIView):
    permission_classes = (IsAdminUser, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsUserOwner,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        try:
            user = User(request.data)
            user.save()

            user_profile = UserProfile(user=user)
            user_profile.save()
            Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileList(generics.ListAPIView):
    permission_classes = (IsAdminUser, )
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


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


def main_view(request):
    return render(request, 'backend/core/main.html')

