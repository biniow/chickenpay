#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^qr/$', views.QrCodeList.as_view()),
    url(r'^qr/(?P<pk>[0-9]+)/$', views.QrCodeList.as_view()),
]
