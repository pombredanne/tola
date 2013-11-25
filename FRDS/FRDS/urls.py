from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FRDS.views.home', name='home'),
    # url(r'^FRDS/', include('FRDS.foo.urls')),

    # enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #read
     url(r'^read/json', 'read.views.getJSON', name='getJSON'),
    
)
