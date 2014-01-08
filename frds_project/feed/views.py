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
from django.core import serializers



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
	
	getFeedType = FeedType.objects.filter(pk = request.POST['feed_type'])
	
	if getFeedType.description == "XML":
		xml = serializers.serialize("xml", getSilo)
		return render(request, 'feed/xml.html', {"xml": "xml"}, content_type="application/xhtml+xml")
	elif getFeedType.description == "JSON":
		jsonData = json.dumps(getSilo)
		return render(request, 'feed/json.html', {"jsonData": "jsonData"}, content_type="application/json")

#DELETE-FEED 
def deleteFeed(request,id):
	
	deleteFeed = Feed.objects.get(pk=id).delete()
	
	return render(request, 'feed/delete.html')		
	
	
	



