from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    ###INDICATOR PLANING TOOL
    #Home
    url(r'^home', 'ipt.views.home', name='home'),
    
    #Dashboard
    url(r'^dashboard', 'ipt.views.dashboard', name='dashboard'),
    
    #Set up Program
    url(r'^program/', 'ipt.views.program', name='program'),
    
    #Edit Program
	url(r'^editProgram/(?P<id>\w+)/$', 'ipt.views.editProgram', name='editProgram'),
	    
    #View Program Indicators
	url(r'^programIndicator/(?P<id>\w+)/$', 'ipt.views.programIndicator', name='programIndicator'),
    
    #Set up Tool
    url(r'^tool', 'ipt.views.program', name='tool'),
    
    #Edit Indicators to Program
    url(r'^editIndicator/(?P<id>\w+)/$', 'ipt.views.editIndicator', name='editIndicator'),
    
    #Add Indicators to Program
    url(r'^indicator', 'ipt.views.indicator', name='indicator'),
    
)