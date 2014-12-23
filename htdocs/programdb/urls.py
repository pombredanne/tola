
from .views import ProjectProposalImport, ProjectProposalList, ProjectProposalCreate, ProjectProposalUpdate, ProjectProposalDelete, ProgramDashboard


try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

# place app url patterns here

urlpatterns = patterns('',

                       ###PROGRAMDB
                       url(r'^dashboard', ProgramDashboard.as_view(), name='dashboard'),

                       #project proposal
                       url(r'^projectproposal_list', ProjectProposalList.as_view(), name='projectproposal_list'),
                       url(r'^projectproposal_add', ProjectProposalCreate.as_view(), name='projectproposal_add'),
                       url(r'^projectproposal_update/(?P<pk>\w+)/$', ProjectProposalUpdate.as_view(), name='projectproposal_update'),
                       url(r'^projectproposal_delete/(?P<pk>\w+)/$', ProjectProposalDelete.as_view(), name='projectproposal_delete'),
                       url(r'^projectproposal_import', ProjectProposalImport.as_view(), name='projectproposal_import'),
                       url(r'^doimport/(?P<pk>\w+)/$', 'programdb.views.doImport' , name='doImport'),
                       url(r'^doMerge/(?P<pk>\w+)/$', 'programdb.views.doMerge', name='doMerge'),


                       )
