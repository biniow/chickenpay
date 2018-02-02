from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import QrCode, Wallet, Transaction, UserProfile
from core.permissions import IsAdminUser, IsUserOwner, IsWalletOwner
from core.serializers import UserProfileSerializer, QrCodeSerializer, WalletSerializer, UserSerializer, \
    RegistrationSerializer, QrCodeGeneratorSerializer


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

    def perform_create(self, serializer):
        serializer.save()
        user_id = serializer.data['id']
        user_profile = UserProfile(user=)
        print(serializer)




class UserProfileList(generics.ListAPIView):
    permission_classes = (IsAdminUser, )
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class QrCodeList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = QrCode.objects.all()
    serializer_class = QrCodeSerializer


class QrCodeDetail(generics.RetrieveAPIView):
    queryset = QrCode.objects.all()
    serializer_class = QrCodeSerializer


class QrCodeCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = QrCode.objects.all()
    serializer_class = QrCodeGeneratorSerializer

    def perform_create(self, serializer):
        date = datetime.now()
        recipient = self.request.user
        serializer.save(date=date, recipient=recipient)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user_id = request.user.id
        amount = serializer.data['amount']
        description = serializer.data['description']
        code = '&$#'.join([str(user_id), str(amount), description])
        response_json = {
            'code': code
        }
        headers = self.get_success_headers(response_json)
        return Response(response_json, status=status.HTTP_201_CREATED, headers=headers)


class WalletList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsWalletOwner, )
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Transaction.objects.all()
    serializer_class = Transaction


class TransactionDetail(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = Transaction


def main_view(request):
    return render(request, 'backend/core/main.html')


def qrcodecreate_view(request):
    return render(request, 'backend/core/qrcode.html')


@login_required
def transaction_view(request):
    transactions = Transaction.objects.filter(sender=request.user)
    return render(request, 'backend/core/transaction.html', {'transactions': transactions})


def registration_view(request):
    return render(request, 'backend/core/registration.html')

