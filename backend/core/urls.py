#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^user/create/$', views.UserCreate.as_view()),
    url(r'^user_profile/$', views.UserProfileList.as_view()),
    url(r'^user_profile/(?P<pk>[0-9]+)/$', views.UserProfileDetail.as_view()),
    url(r'^qr/$', views.QrCodeList.as_view()),
    url(r'^qr/(?P<pk>[0-9]+)/$', views.QrCodeDetail.as_view()),
    url(r'^qr/create/$', views.QrCodeCreate.as_view()),
    url(r'^wallet/$', views.WalletList.as_view()),
    url(r'^wallet/(?P<pk>[0-9]+)/$', views.WalletDetail.as_view()),
    url(r'^transaction/$', views.TransactionList.as_view()),
    url(r'^transaction/(?P<pk>[0-9]+)/$', views.TransactionDetail.as_view()),
]
