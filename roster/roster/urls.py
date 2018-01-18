"""roster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login
from django.contrib import admin
from teacher.views import teacher1,home,yoyo,master_tt,Lab1,Room1
from semclass.views import master
from location.views import classroom,lab
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^home/$', home, name = 'home'),
    url(r'^$', home, name = 'home'),
    url(r'^teacher1/$',teacher1, name = 'teacher1'),
    url(r'^master/$',master, name = 'master'),
    url(r'^classroom/$',classroom, name = 'classroom'),
    url(r'^lab/$',lab, name = 'lab'),
    url(r'^(?P<string1>[\w\-]+)/teacher/(?P<id>[0-99]{1,2})/$', yoyo, name='yoyo'),
    url(r'^(?P<string1>[\w\-]+)/Lab/(?P<id>[0-99]{1,2})/$', Lab1, name='Lab1'),
    url(r'^(?P<string1>[\w\-]+)/Class_Room/(?P<id>[0-99]{1,2})/$', Room1, name='Room1'),
    url(r'^(?P<string2>[\w\-]+)/master/(?P<id>[0-99]{1,2})/Semester/(?P<string4>[\w\-]+)/Section/$', master_tt, name='master_tt'),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


