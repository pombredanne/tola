from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
import os
from django.http import HttpResponseRedirect
from django.db import models
from silo.models import Silo, DataField, ValueStore
from feed.serializers import FeedSerializer,FeedInstanceSerializer
from feed.models import Feed
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
	Get all Silos and Link to REST API pages
	"""
	#get all of the silos
	getSilos = Silo.objects.all()

	return render(request, 'feed/list.html',{'getSilos': getSilos})

class Feed(generics.ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class FeedInstance(generics.RetrieveAPIView):
    queryset = Silo.objects.all()
    serializer_class = FeedInstanceSerializer

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

	
	



