# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url, include

import spirit.comment.bookmark.urls
import spirit.comment.flag.urls
import spirit.comment.history.urls
import spirit.comment.like.urls
import spirit.comment.poll.urls
from . import views


urlpatterns = [
    url(r'^(?P<topic_id>\d+)/publicar/$', views.publish, name='publish'),
    url(r'^(?P<topic_id>\d+)/publicar/(?P<pk>\d+)/citar/$', views.publish, name='publish'),

    url(r'^(?P<pk>\d+)/actualizar/$', views.update, name='update'),
    url(r'^(?P<pk>\d+)/encontrar/$', views.find, name='find'),
    url(r'^(?P<topic_id>\d+)/mover/$', views.move, name='move'),

    url(r'^(?P<pk>\d+)/borrar/$', views.delete, name='delete'),
    url(r'^(?P<pk>\d+)/noborrar/$', views.delete, kwargs={'remove': False, }, name='undelete'),

    url(r'^subir/$', views.image_upload_ajax, name='image-upload-ajax'),

    url(r'^marcador/', include(spirit.comment.bookmark.urls, namespace='bookmark')),
    url(r'^bandera/', include(spirit.comment.flag.urls, namespace='flag')),
    url(r'^historia/', include(spirit.comment.history.urls, namespace='history')),
    url(r'^megusta/', include(spirit.comment.like.urls, namespace='like')),
    url(r'^encuesta/', include(spirit.comment.poll.urls, namespace='poll')),
]
