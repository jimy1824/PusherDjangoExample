"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from django.urls import path
from message.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(),{'template_name': 'login.html'}),
    # url(r'^login/$', views.login, {'template_name': 'login.html'}),
    # url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'^conversation$', broadcast),
    url(r'^conversations/$', conversations),
    url(r'^conversations/(?P<id>[-\w]+)/delivered$', delivered)
]
