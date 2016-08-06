# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth import views as django_views
from django.core.urlresolvers import reverse_lazy

from . import views


urlpatterns = [
	url(r'^iniciar-sesion/$', views.custom_login, {'template_name': 'spirit/user/auth/login.html'}, name='login'),
	url(r'^cerrar-sesion/$', views.custom_logout, {'next_page': '/', }, name='logout'),
	url(r'^registro/$', views.register, name='register'),
	#url(r'^reenviar-activacion/$', views.resend_activation_email, name='resend-activation'),
	#url(r'^activacion/(?P<pk>\d+)/(?P<token>[0-9A-Za-z_\-\.]+)/$', views.registration_activation, name='registration-activation'),

	#url(r'^restablecer-contraseña/$', views.custom_password_reset,
	#	{
	#		'template_name': 'spirit/user/auth/password_reset_form.html',
	#		'email_template_name': 'spirit/user/auth/password_reset_email.html',
	#		'subject_template_name': 'spirit/user/auth/password_reset_subject.txt',
	#		'post_reset_redirect': reverse_lazy('spirit:user:auth:password-reset-done')
	#	}, name='password-reset'),
	#
	#url(r'^restablecer-contraseña/hecho/$', django_views.password_reset_done, {'template_name': 'spirit/user/auth/password_reset_done.html', }, name='password-reset-done'),
	#url(r'^reinicio/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[\w\-]+)/$', django_views.password_reset_confirm,
	#	{
	#		'template_name': 'spirit/user/auth/password_reset_confirm.html',
	#		'post_reset_redirect': reverse_lazy('spirit:user:auth:password-reset-complete')
	#	}, name='password-reset-confirm'),
	#url(r'^reinicio/hecho/$', django_views.password_reset_complete, {'template_name': 'spirit/user/auth/password_reset_complete.html', }, name='password-reset-complete'),
]
