# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import include, url, patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.views import serve

import spirit.urls

# Override admin login for security purposes
from django.contrib.auth.decorators import login_required
admin.site.login = login_required(admin.site.login)


urlpatterns = [
	url(r'^admindjango/', include(admin.site.urls)),
	url(r'^', include(spirit.urls)),
	#url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

