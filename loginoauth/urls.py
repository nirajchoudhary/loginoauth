from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('logintest.views',

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'checkLoginStatus'),
	#url(r'^loginhtml/$', TemplateView.as_view(template_name = 'login.html')),
	#url(r'^loggedin/$', TemplateView.as_view(template_name = 'loggedin.html')),
	url(r'^login/$', 'login'),
	url(r'^details/$', 'insertDetails'),
	url(r'^logout/$', 'logout'),
	#url(r'^link/$', TemplateView.as_view(template_name = 'oAuthSignup.html')),
	url(r'^olduser/$', 'oldUserLogin'),
	url(r'^newuser/$', 'NewUserLogin'),
)
