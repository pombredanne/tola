from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
import os
from django.http import HttpResponseRedirect
from django.db import models
from silo.models import Silo, DataField, ValueStore, ValueType, Read, Feed
from django.shortcuts import render_to_response
import dicttoxml


#Create a form to get feed info then save data to Read and re-direct to getJSON funtion
def listFeeds(request):
	#get all of the silos
	getFeeds = Feed.objects.all()
	
	#get all of the silos
	getSources = Silo.objects.all()

	return render(request, 'feed/list.html',{'getSources':getSources,'getFeeds':getFeeds})

def exportToXml(request):
	#getSilo data to export to Feed
	getSilo = Silo.objects.all().filter(id=silo_id)
	
	xml = dicttoxml.dicttoxml(some_dict)
	
	return render(request, 'feed/xml.html', {"xml": "xml"}, content_type="application/xhtml+xml")
	



