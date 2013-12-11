from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
import os
from django.http import HttpResponseRedirect
from django.db import models
from silo.models import Silo, DataField, ValueStore, ValueType
from django.shortcuts import render_to_response

#Create a form to get feed info then save data to Read and re-direct to getJSON funtion
def listSilos(request):
	#get all of the silos
	get_silo = Silo.objects.all()

	return render(request, 'silos.html',{'get_silo':get_silo})


#get JSON feed info from form then grab data
def listSiloSources(request):
	
	#get fields to display back to user for verification
	getSources = Silo.objects.filter(silo_id=silo_id)
	
	#send the keys and vars from the json data to the template along with submitted feed info and silos for new form				
	return render_to_response("stores.html", {'getSilo':getSilo,'silo_id':silo_id})


#get JSON feed info from form then grab data
def showStore(request):
	silo_id = request.GET.get('id')
	#get fields to display back to user for verification
	getFields = DataField.objects.filter(silo__pk=silo_id)
	
	#send the keys and vars from the json data to the template along with submitted feed info and silos for new form				
	return render_to_response("stored_values.html", {'getFields':getFields})

