# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url, include

import spirit.topic.moderate.urls
import spirit.topic.unread.urls
import spirit.topic.notification.urls
import spirit.topic.favorite.urls
import spirit.topic.private.urls
import spirit.topic.poll.urls
from . import views


urlpatterns = [
    url(r'^publicar/$', views.publish, name='publish'),
    url(r'^publicar/(?P<category_id>\d+)/$', views.publish, name='publish'),

    url(r'^actualizar/(?P<pk>\d+)/$', views.update, name='update'),

    url(r'^(?P<pk>\d+)/$', views.detail, kwargs={'slug': "", }, name='detail'),
    url(r'^(?P<pk>\d+)/(?P<slug>[\w-]+)/$', views.detail, name='detail'),

    url(r'^activo/$', views.index_active, name='index-active'),

    url(r'^moderar/', include(spirit.topic.moderate.urls, namespace='moderate')),
    url(r'^noleido/', include(spirit.topic.unread.urls, namespace='unread')),
    url(r'^notificacion/', include(spirit.topic.notification.urls, namespace='notification')),
    url(r'^favorito/', include(spirit.topic.favorite.urls, namespace='favorite')),
    url(r'^privado/', include(spirit.topic.private.urls, namespace='private')),
    url(r'^encuesta/', include(spirit.topic.poll.urls, namespace='poll')),  # todo: remove me!
]
