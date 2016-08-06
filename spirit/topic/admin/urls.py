# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.deleted, name='index'),
    url(r'^eliminado/$', views.deleted, name='deleted'),
    url(r'^cerrado/$', views.closed, name='closed'),
    url(r'^pinned/$', views.pinned, name='pinned'),
]
