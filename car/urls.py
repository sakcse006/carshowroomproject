"""carproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^cars/$',views.cars,name='cars'),
    url(r'^spare/$',views.spare,name='spare'),
    url(r'^service/$',views.service,name='service'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^toyota/$',views.toyota,name='toyota'),
    url(r'^hyundai/$',views.hyundai,name='hyundai'),
    url(r'^ford/$',views.ford,name='ford'),
    url(r'^nissan/$',views.nissan,name='nissan'),
    url(r'^honda/$',views.honda,name='honda'),
    url(r'^audi/$',views.audi,name='audi'),
    url(r'^bmw/$',views.bmw,name='bmw'),
    url(r'^rollsroyce/$',views.rollsroyce,name='rollsroyce'),
    url(r'^marutisuzuki/$',views.marutisuzuki,name='marutisuzuki'),
    url(r'^tata/$',views.tata,name='tata'),
    url(r'^gear/$',views.gear,name='gear'),
    url(r'^door/$',views.door,name='door'),
    url(r'^hyst/$',views.hyst,name='hyst'),
    url(r'^msbumper/$',views.msbumper,name='msbumper'),
    url(r'^nw/$',views.nw,name='nw'),

]
