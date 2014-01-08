from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    ###INDICATOR PLANING TOOL
    #Home
    url(r'^home', 'ipt.views.home', name='home'),
    
    #Dashboard
    url(r'^dashboard', 'ipt.views.dashboard', name='dashboard'),
    
    #Set up Program
    url(r'^program', 'ipt.views.program', name='program'),
    
    #Set up Tool
    url(r'^tool', 'ipt.views.program', name='tool'),
    
    #Add Indicators to Program
    url(r'^indicator', 'ipt.views.indicator', name='indicator'),
    
)