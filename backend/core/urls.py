#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from core import views

urlpatterns = [
    url(r'^$', views.main_view),
    url(r'^dashboard', views.dashboard_view),
    url(r'^transactions/', views.transaction_view),
    url(r'^qrcodecreate/', views.qrcodecreate_view),
    url(r'^qrcode/(?P<pk>[0-9]+)/', views.qrcode_details_view),
    url(r'^qrcodeList/', views.qrcodelist_view),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': '/logged_out/'}),

]
