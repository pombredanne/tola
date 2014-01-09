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
	url(r'^read', 'read.views.home', name='home'),
	
	#read init form
	url(r'^new_read', 'read.views.initRead', name='initRead'),
	
	#show read or source
	url(r'^show_read/(?P<id>\w+)/$', 'read.views.showRead', name='showRead'),

	#login form
	url(r'^login', 'read.views.getLogin', name='getLogin'),

	#getJSON data
	url(r'^json', 'read.views.getJSON', name='getJSON'),

	#updateUID data
	url(r'^update', 'read.views.updateUID', name='updateUID'),

	###DISPLAY
	#list all silos
	url(r'^silos', 'display.views.listSilos', name='listSilos'),

	#show silo detail and sources
	url(r'^silo/(?P<id>\w+)/$', 'display.views.viewSilo', name='viewSilo'),
	
	#merge form
	url(r'^merge/(?P<id>\w+)/$', 'display.views.mergeForm', name='mergeForm'),
	
	#merge select columns
	url(r'^merge_columns', 'display.views.mergeColumns', name='mergeColumns'),

	#list all silos
	url(r'^display', 'display.views.listSilos', name='listSilos'),

	#view silo detail
	url(r'^silo_detail/(?P<id>\w+)/$', 'display.views.showStore', name='showStore'),

	###SILO
	url(r'^do_merge', 'silo.views.doMerge', name='doMerge'),
	
	#edit silo
	url(r'^silo_edit/(?P<id>\w+)/$', 'silo.views.editSilo', name='editSilo'),
	
	#merge silos
	url(r'^doMerge', 'silo.views.doMerge', name='doMerge'),
	
	#delete a silo
	url(r'^silo_delete/(?P<id>\w+)/$','silo.views.deleteSilo', name='deleteSilo'),

	###FEED
	url(r'^feed', 'feed.views.listFeeds', name='listFeeds'),
	
	#create a feed
	url(r'^create_feed', 'feed.views.createFeed', name='createFeed'),
	
	#delete a feed
	url(r'^feed_delete','feed.views.deleteFeed', name='deleteFeed'),

)
