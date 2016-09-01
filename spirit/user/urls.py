# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url, include


from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^preferencias/$', views.update, name='update'),
    url(r'^cambiar-contraseña/$', views.password_change, name='password-change'),
    url(r'^cambiar-email/$', views.email_change, name='email-change'),
    url(r'^cambiar-email/(?P<token>[0-9A-Za-z_\-\.]+)/$', views.email_change_confirm, name='email-change-confirm'),

    url(r'^(?P<pk>\d+)/$', views.comments, kwargs={'slug': "", }, name='detail'),
    url(r'^(?P<pk>\d+)/(?P<slug>[\w-]+)/$', views.comments, name='detail'),

    url(r'^temas/(?P<pk>\d+)/$', views.topics, kwargs={'slug': "", }, name='topics'),
    url(r'^temas/(?P<pk>\d+)/(?P<slug>[\w-]+)/$', views.topics, name='topics'),

    url(r'^megusta/(?P<pk>\d+)/$', views.likes, kwargs={'slug': "", }, name='likes'),
    url(r'^megusta/(?P<pk>\d+)/(?P<slug>[\w-]+)/$', views.likes, name='likes'),

    url(r'^menu/$', views.menu, name='menu'),

    
]