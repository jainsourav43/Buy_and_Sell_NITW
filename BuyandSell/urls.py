from django.conf.urls import url
from django.contrib import admin
from .import views

app_name ='BuyandSell'

urlpatterns = [
    url(r'^Buy/$', views.home,name='main'),
    url(r'^login_user/$', views.login_user,name='login_user'),
    url(r'^(?P<username>[a-zA_Z0-9]+)/sell/$', views.sell,name='sell'),
    url(r'^(?P<username>[a-zA_Z0-9]+)/profile/$', views.profile,name='profile'),
    url(r'^(?P<username>[a-zA_Z0-9]+)/$', views.test,name='test'),
]

