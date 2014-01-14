from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
import os
from django.http import HttpResponseRedirect
from django.db import models
from silo.models import Silo, DataField, ValueStore, ValueType, Read, Feed
from feed.models import FeedType
from django.shortcuts import render_to_response
import dicttoxml,json
import unicodedata
from django.core import serializers
from django.utils import simplejson
from frds_project.util import siloToDict



#Feeds
def listFeeds(request):
	
	#get all of the silos
	getFeeds = Feed.objects.all()
	
	#get all of the silos
	getSources = Silo.objects.all()
	
	#get all of the silos
	getFeedTypes = FeedType.objects.all()

	return render(request, 'feed/list.html',{'getFeeds': getFeeds,'getSources': getSources, 'getFeedTypes': getFeedTypes})

def createFeed(request):

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
	
	deleteFeed = Feed.objects.get(pk=id).delete()
	
	return render(request, 'feed/delete.html')		
	

#XML for non Model Object Serialization
def serialize(root):
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

	
	



