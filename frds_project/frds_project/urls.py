from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #read init form
    url(r'^read', 'read.views.initRead', name='initRead'),
    
    #getJSON data
     url(r'^json', 'read.views.getJSON', name='getJSON'),
)
