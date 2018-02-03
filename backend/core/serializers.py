#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import QrCode, Wallet, Transaction, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'password', 'groups', 'user_permissions', 'is_staff',
                  'is_active', 'is_superuser', 'last_login', 'date_joined')


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'password')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'bank_account_number', 'address', 'pin_code',
                  'max_daily_transfer_amount')


class QrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCode
        fields = ('id', 'recipient', 'amount', 'description')


class QrCodeGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCode
        fields = ('id', 'amount', 'description')


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'user', 'balance')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'sender', 'recipient', 'amount', 'completed', 'date')


class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'recipient', 'amount')
