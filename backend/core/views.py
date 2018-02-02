from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import QrCode, Wallet, Transaction, UserProfile
from core.permissions import IsAdminUser, IsQrCodeOwner, IsWalletOwner
from core.serializers import UserProfileSerializer, QrCodeSerializer, WalletSerializer, UserSerializer, \
    RegistrationSerializer, QrCodeGeneratorSerializer


class UserList(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get_queryset(self):
        return [self.request.user]


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

        user_profile = UserProfile(user=instance)
        user_profile.save()

        wallet = Wallet(user=instance)
        wallet.balance = 0.0
        wallet.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_json = serializer.data
        response_json.pop('password')
        headers = self.get_success_headers(response_json)
        return Response(response_json, status=status.HTTP_201_CREATED, headers=headers)


class UserProfileList(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)


class QrCodeList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QrCodeSerializer

    def get_queryset(self):
        user = self.request.user
        return QrCode.objects.filter(recipient=user)


class QrCodeDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = QrCodeSerializer

    def get_queryset(self):
        user = self.request.user
        return QrCode.objects.filter(recipient=user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        user_id = request.user.id
        amount = serializer.data['amount']
        description = serializer.data['description']
        code = '&$#'.join([str(user_id), str(amount), description])
        response_json = serializer.data
        response_json['code'] = code
        return Response(response_json)


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
    permission_classes = (IsAuthenticated, )
    serializer_class = WalletSerializer

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(user=user)


class TransactionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = Transaction

    def get_queryset(self):
        user = self.request.user
        as_recipient = Transaction.objects.filter(recipient=user)
        as_sender = Transaction.objects.filter(sender=user)
        return as_recipient + as_sender


class TransactionDetail(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = Transaction



def main_view(request):
    return render(request, 'backend/core/main.html')


def qrcodecreate_view(request):
    return render(request, 'backend/core/qrcode.html')


@login_required
def transaction_view(request):
    transactions = Transaction.objects.get(sender=request.user)
    return render(request, 'backend/core/transaction.html', {'transactions': transactions})

