#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from core.models import QrCode, Wallet, Transaction, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'password', 'groups', 'user_permissions', 'is_staff',
                  'is_active', 'is_superuser', 'last_login', 'date_joined',
                  'bank_account_number', 'address', 'pin_code',
                  'max_daily_transfer_amount')


class QrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCode
        fields = ('id', 'recipient', 'amount', 'date', 'description')


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'user', 'balance')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'sender', 'recipient', 'amount', 'completed', 'date')
