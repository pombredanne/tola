from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
import os
from django.http import HttpResponseRedirect
from django.db import models
from silo.models import Silo, DataField, ValueStore
from feed.serializers import SiloSerializer,DataFieldSerializer,ValueStoreSerializer
from feed.models import Feed
from django.shortcuts import render_to_response
import dicttoxml,json
import unicodedata
from django.core import serializers
from django.utils import simplejson
from asana.util import siloToDict
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import renderers,viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import link, api_view
from rest_framework.views import APIView
from rest_framework import filters
from itertools import chain
import operator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
  	"""
  	deleteFeed = Feed.objects.get(pk=id).delete()

  	return render(request, 'feed/delete.html')
