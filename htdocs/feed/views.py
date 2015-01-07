from silo.models import Silo, DataField, ValueStore
from read.models import Read, ReadType
from .serializers import SiloSerializer, DataFieldSerializer, ValueStoreSerializer, UserSerializer, ReadSerializer, ReadTypeSerializer

from django.contrib.auth.decorators import login_required
import json as simplejson
from tola.util import siloToDict

from django.template import RequestContext
from django.contrib.auth.models import User


from rest_framework import renderers,viewsets

import operator
import csv


from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden,\
    HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest,\
    HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect, render

# API Classes


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SiloViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Silo.objects.all()
    serializer_class = SiloSerializer

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

class ReadViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Read.objects.all()
    serializer_class = ReadSerializer

class ReadTypeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ReadType.objects.all()
    serializer_class = ReadTypeSerializer

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

from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage
from oauth2client import xsrfutil
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from .models import GoogleCredentialsModel
from apiclient.discovery import build
import os, logging, httplib2, json, datetime

CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')
FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/drive',
    redirect_uri='http://localhost:8000/oauth2callback/')

@login_required
def google_export(request):
    storage = Storage(GoogleCredentialsModel, 'id', request.user, 'credential')
    credential = storage.get()
    if credential is None or credential.invalid == True:
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY, request.user)
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)
    else:
        http = httplib2.Http()
        http = credential.authorize(http)
        service = build("drive", "v2", http=http)
        body = {
            'title': "GOOGLE SPREADSHEET-OK",
            'description': "TEST FILE FROM API",
            'mimeType': "application/vnd.google-apps.spreadsheet"
        }
        file = service.files().insert(body=body).execute()
        return HttpResponse(json.dumps(file), content_type="application/json")
        #https://developers.google.com/drive/v2/reference/files/get
        #https://developers.google.com/google-apps/spreadsheets/#creating_a_spreadsheet
    return HttpResponse("OK")

@login_required
def oauth2callback(request):
    if not xsrfutil.validate_token(settings.SECRET_KEY, request.REQUEST['state'], request.user):
        return  HttpResponseBadRequest()

    credential = FLOW.step2_exchange(request.REQUEST)
    storage = Storage(GoogleCredentialsModel, 'id', request.user, 'credential')
    storage.put(credential)
    #print(credential.to_json())
    return HttpResponseRedirect("/")
