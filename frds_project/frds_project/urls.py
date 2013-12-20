from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='base.html')),

	#ipt app specific urls
	url(r'^ipt/', include('ipt.urls')),

	#enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	#enable the admin:
	url(r'^admin/', include(admin.site.urls)),

	#home
	url(r'^home', 'display.views.listSilos', name='listSilos'),

	###READ
	#read init form
	url(r'^read', 'read.views.initRead', name='initRead'),

	#login form
	url(r'^login', 'read.views.getLogin', name='getLogin'),

	#getJSON data
	url(r'^json', 'read.views.getJSON', name='getJSON'),

	#updateUID data
	url(r'^update', 'read.views.updateUID', name='updateUID'),

	###DISPLAY
	#List all Silos
	url(r'^silos', 'display.views.listSilos', name='listSilos'),

	#Show Silo Detail and Sources
	url(r'^silo/(?P<id>\w+)/$', 'display.views.viewSilo', name='viewSilo'),
	
	#Merge Form
	url(r'^merge/(?P<id>\w+)/$', 'display.views.mergeForm', name='mergeForm'),
	
	#Merge select columns
	url(r'^merge_columns', 'display.views.mergeColumns', name='mergeColumns'),

	#List all Silos
	url(r'^display', 'display.views.listSilos', name='listSilos'),

	#View Silo Detail
	url(r'^silo_detail/(?P<id>\w+)/$', 'display.views.showStore', name='showStore'),

	###SILO
	url(r'^do_merge', 'silo.views.doMerge', name='doMerge'),
	
	#Edit Silo
	url(r'^silo_edit/(?P<id>\w+)/$', 'silo.views.editSilo', name='editSilo'),
	
	#Merge Silos
	url(r'^doMerge', 'silo.views.doMerge', name='doMerge'),

	###FEED
	url(r'^feed', 'feed.views.listFeeds', name='listFeeds'),

)
