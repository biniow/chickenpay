from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from core.models import User, QrCode
from core.serializers import UserSerializer, QrCodeSerializer


class UserList(generics.ListCreateAPIView):
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
