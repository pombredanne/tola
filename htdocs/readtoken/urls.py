from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

                       ###READ
                       #read init form
                       url(r'^home', 'readtoken.views.home', name='home'),

                       #read init form
                       url(r'^new_read', 'readtoken.views.initRead', name='initRead'),

                       #show read or source
                       url(r'^show_read/(?P<id>\w+)/$', 'readtoken.views.showRead', name='showRead'),

                       #getJSON data
                       url(r'^json', 'readtoken.views.getJSON', name='getJSON'),

                       #updateUID data
                       url(r'^update', 'readtoken.views.updateUID', name='updateUID'),

                       #silo form
                       url(r'^silo/(?P<id>\w+)/$', 'readtoken.views.getSilo', name='getSilo'),

                       )

