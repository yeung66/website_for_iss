"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from signup.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^index', index),
    url(r'^Creativity', intro_creativity, name='intro_creativity'),
    url(r'^Mobile-coding', intro_mobile, name='intro_mobile'),
    url(r'^Hackathon', intro_hack, name='intro_hack'),
    url(r'^Notice1', notice_crea, name='notice_crea'),
    url(r'^Notice2', notice_mobile, name='notice_mobile'),
    url(r'^Notice3', notice_hack, name='notice_hack'),

    url(r'^submitWork', submitWork, name='submitWork'),
    url(r'^signup_crea', signup_crea, name='signup_crea'),
    url(r'^signup_malasong', signup_malasong, name='signup_malasong'),
    url(r'signup_shouji', signup_shouji, name='signup_shouji'),
]
