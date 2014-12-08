from silo.models import Silo, DataField, ValueStore
from feed.serializers import SiloSerializer,DataFieldSerializer,ValueStoreSerializer
from feed.models import Feed
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from tola.util import siloToDict
from google import google_export_xls
from django.template import RequestContext

from rest_framework import renderers,viewsets

import operator
import csv

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden,\
    HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest,\
    HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect, render

# API Classes


class FeedViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Silo.objects.all()
    serializer_class = SiloSerializer


class DataFieldViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = DataField.objects.all()
    serializer_class = DataFieldSerializer


class ValueStoreViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ValueStore.objects.all()
    serializer_class = ValueStoreSerializer

# End API Classes


def customFeed(request,id):
    """
    All tags in use on this system
    id = Silo
    """
    #get all of the data fields for the silo
    queryset = DataField.objects.filter(silo__id=id)

    formatted_data = []

    #loop over the labels and populate the first list with lables
    for label in queryset:
        #append the label to the list
        formatted_data.append(label.name)
        valueset = ValueStore.objects.filter(field__id=label.id)
        #loop over the values and append the values for each label
        for val in valueset:
            formatted_data.append(val.char_store)

    #output list to json
    jsonData = simplejson.dumps(formatted_data)
    return render(request, 'feed/json.html', {"jsonData": jsonData}, content_type="application/json")

#Feeds
def listFeeds(request):
    """
    Get all Silos and Link to REST API pages
    """
    #get all of the silos
    getSilos = Silo.objects.all()

    return render(request, 'feed/list.html',{'getSilos': getSilos})

def createFeed(request):
    """
    Create an XML or JSON Feed from a given Silo
    """
    getSilo = ValueStore.objects.filter(field__silo__id=request.POST['silo_id'])

    #return a dict with label value pair data
    formatted_data = siloToDict(getSilo)

    getFeedType = FeedType.objects.get(pk = request.POST['feed_type'])

    if getFeedType.description == "XML":
        xmlData = serialize(formatted_data)
        return render(request, 'feed/xml.html', {"xml": xmlData}, content_type="application/xhtml+xml")
    elif getFeedType.description == "JSON":
        jsonData = simplejson.dumps(formatted_data)
        return render(request, 'feed/json.html', {"jsonData": jsonData}, content_type="application/json")

def export_silo(request, id):
    """
    Export a silo to a CSV file
    id = Silo
    """
    getSiloRows = ValueStore.objects.all().filter(field__silo__id=id).values('row_number').distinct()
    getColumns = DataField.objects.all().filter(silo__id=id).values('name').distinct()

    #return a dict with label value pair data
    #formatted_data = siloToDict(getSilo)

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    getSiloName = Silo.objects.get(pk=id)
    file = getSiloName.name + ".csv"

    response['Content-Disposition'] = 'attachment; filename=file'

    writer = csv.writer(response)

    #create a list of column names
    column_list = []
    value_list = []
    for column in getColumns:
        column_list.append(str(column['name']))
    #print the list of column names
    writer.writerow(column_list)

    #loop over each row of the silo
    for row in getSiloRows:
        getSiloColumns = ValueStore.objects.all().filter(field__silo__id=id, row_number=str(row['row_number'])).values_list('field__name', flat=True).distinct()
        print "row"
        print str(row['row_number'])
        #get a column value for each column in the row
        for x in column_list:
            if x in getSiloColumns:
                print x
                getSiloValues = ValueStore.objects.get(field__silo__id=id, row_number=str(row['row_number']), field__name=x)
                value_list.append(str(getSiloValues.char_store.encode(errors="ignore")))
            else:
                value_list.append("")


        #print the row
        writer.writerow(value_list)
        value_list = []



    return response


def createDynamicModel(request):
    """
    Create an XML or JSON Feed from a given Silo
    """
    getSilo = Silo.objects.filter(silo_id=request.POST['silo_id'])
    getValues = ValueStore.objects.filter(field__silo__id=request.POST['silo_id'])
    getFields = DataField.objects.filter(field__silo__id=request.POST['silo_id'])

    #return a dict with label value pair data
    formatted_data = siloToModel(getSilo['name'],getFields['name'])

    getFeedType = FeedType.objects.get(pk = request.POST['feed_type'])

    if getFeedType.description == "XML":
        xmlData = serialize(formatted_data)
        return render(request, 'feed/xml.html', {"xml": xmlData}, content_type="application/xhtml+xml")
    elif getFeedType.description == "JSON":
        jsonData = simplejson.dumps(formatted_data)
        return render(request, 'feed/json.html', {"jsonData": jsonData}, content_type="application/json")


#DELETE-FEED
def deleteFeed(request,id):
    """
    Delete a feed
    id = Feed
    """
    deleteFeed = Feed.objects.get(pk=id).delete()

    return render(request, 'feed/delete.html')


def _get_google_token(request, redirect_to_url):
    """
    Get token for google user
    """
    token = None
    if request.user.is_authenticated():
        try:
            ts = TokenStorageModel.objects.get(id=request.user)
        except TokenStorageModel.DoesNotExist:
            pass
        else:
            token = ts.token
    elif request.session.get('access_token'):
        token = request.session.get('access_token')
    if token is None:
        request.session["google_redirect_url"] = redirect_to_url
        return HttpResponseRedirect(redirect_uri)
    return token

#@login_required
def export_google(request, id):
    """
    Export a silo to google
    id = Silo
    """
    context = RequestContext(request)
    context.username = request.user

    exports = ValueStore.objects.filter(field__silo__id=id)
    context.exports = exports
    google_export_xls(filename, exports.silo_name, token, exports)
    return render_to_response('export_list.html', context_instance=context)
