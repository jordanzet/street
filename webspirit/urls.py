from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static


from home import views
from home import urls as home_urls
from course import urls as course_urls
from university import urls as university_urls
from student import urls as student_urls


urlpatterns = [
	# Examples:
	# url(r'^$', 'spirit.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	#url(r'^admin/', admin.site.urls),
	url(r'^$', views.home, name='home'),
	url(r'^', include(home_urls)),
	url(r'^', include(course_urls, namespace="course")),
	url(r'^', include(student_urls, namespace="student")),
	url(r'^', include(university_urls, namespace="university")),
	url(r'^ckeditor/', include('ckeditor_uploader.urls')),
	url(r'^static/(?P<path>.*)$', serve),
	#url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
