# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^actualizar/(?P<pk>\d+)/$', views.update, name='update'),
    url(r'^cerrar/(?P<pk>\d+)/$', views.close, name='close'),
    url(r'^votar/(?P<pk>\d+)/$', views.vote, name='vote'),
]
