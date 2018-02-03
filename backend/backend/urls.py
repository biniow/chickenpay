"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api/', include('core.urls')),
    url(r'^main/', views.main_view),
    url(r'^transactions/', views.transaction_view),
    url(r'^qrcodecreate/', views.qrcodecreate_view),
    url(r'^registration/', views.registration_view),
    url(r'^qrcode/(?P<pk>[0-9]+)/', views.qrcode_details_view),
    url(r'^qrcodeList/', views.qrcodelist_view),

]
