# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import include, url

import spirit.topic.views
import spirit.admin.urls
import spirit.user.urls
import spirit.search.urls
import spirit.category.urls
import spirit.topic.urls
import spirit.comment.urls


patterns = [
    url(r'^$', spirit.topic.views.index_active, name='index'),
    url(r'^admin/', include(spirit.admin.urls, namespace='admin')),
    url(r'^usuario/', include(spirit.user.urls, namespace='user')),
    url(r'^buscar/', include(spirit.search.urls, namespace='search')),
    url(r'^categoria/', include(spirit.category.urls, namespace='category')),
    url(r'^pregunta/', include(spirit.topic.urls, namespace='topic')),
    url(r'^comentario/', include(spirit.comment.urls, namespace='comment')),
]


urlpatterns = [
    url(r'^', include(patterns, namespace='spirit', app_name='spirit')),
]
