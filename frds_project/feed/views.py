from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
import os
from django.http import HttpResponseRedirect
from django.db import models
from silo.models import Silo, DataField, ValueStore, Read, Feed
from feed.models import FeedType
from feed.serializers import FeedSerializer
from django.shortcuts import render_to_response
import dicttoxml,json
import unicodedata
from django.core import serializers
from django.utils import simplejson
from frds_project.util import siloToDict
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

#Feeds
def listFeeds(request):
	"""
	Get all Feeds and sources and display them
	"""
	#get all of the silos
	getFeeds = Feed.objects.all()
	
	#get all of the silos
	getSources = Silo.objects.all()
	
	#get all of the silos
	getFeedTypes = FeedType.objects.all()

	return render(request, 'feed/list.html',{'getFeeds': getFeeds,'getSources': getSources, 'getFeedTypes': getFeedTypes})

class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = ValueStore.objects.all()
    serializer_class = FeedSerializer
    paginate_by = None

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

#DELETE-FEED 
def deleteFeed(request,id):
	"""
	DELETE A FEED
	"""
	deleteFeed = Feed.objects.get(pk=id).delete()
	
	return render(request, 'feed/delete.html')		
	

#XML for non Model Object Serialization
def serialize(root):
	"""
	Create an XML formatted dictionary object based on a queryset
	"""
	xml = ''
	for key in root.keys():
		if isinstance(root[key], dict):
			xml = '%s<%s>\n%s</%s>\n' % (xml, key, serialize(root[key]), key)
		elif isinstance(root[key], list):
			xml = '%s<%s>' % (xml, key)
			for item in root[key]:
				xml = '%s%s' % (xml, serialize(item))
			xml = '%s</%s>' % (xml, key)
		else:
			value = root[key]
			xml = '%s<%s>%s</%s>\n' % (xml, key, value, key)
	return xml

	
	



