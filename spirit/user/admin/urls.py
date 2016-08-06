# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^administrador/$', views.index_admins, name='index-admins'),
    url(r'^moderador/$', views.index_mods, name='index-mods'),
    url(r'^inactivo/$', views.index_unactive, name='index-unactive'),
    url(r'^editar/(?P<user_id>\d+)/$', views.edit, name='edit'),
]
