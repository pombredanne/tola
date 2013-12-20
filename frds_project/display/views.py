from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
import os
from django.http import HttpResponseRedirect
from django.db import models
from silo.models import Silo, DataField, ValueStore, ValueType, Read
from django.shortcuts import render_to_response
import django_tables2 as tables

#SILOS
def listSilos(request):
	
	#get all of the silos
	get_silos = Silo.objects.all()

	return render(request, 'display/silos.html',{'get_silos':get_silos})

#SILO-SOURCES
def listSiloSources(request):
	
	#get fields to display back to user for verification
	getSources = Read.objects.filter(silo_id=silo_id)
	
	#send the keys and vars from the json data to the template along with submitted feed info and silos for new form				
	return render_to_response("display/stores.html", {'getSilo':getSilo,'silo_id':silo_id})

#Display Silo
def viewSilo(request,id):
	
	silo_id = id
	#get all of the silos
	get_sources = Read.objects.all().filter(silo__id=silo_id)

	return render(request, 'display/silo-sources.html',{'get_sources':get_sources})

#SILO-SOURCES Show data from source
def showStore(request,id):
	
	silo_id = id
	getSilo = ValueStore.objects.all().filter(field__silo_id=silo_id)
	
	#send the keys and vars from the json data to the template along with submitted feed info and silos for new form				
	return render(request,"display/stored_values.html", {'getSilo':getSilo})
	
#SHOW-MERGE
def mergeForm(request,id):
	
	getSource = Silo.objects.get(id=id)
	getSourceTo = Silo.objects.all()
	return render_to_response("display/merge-form.html", {'getSource':getSource,'getSourceTo':getSourceTo})

def mergeColumns(request):
	
	from_silo_id = request.POST["from_silo_id"]
	to_silo_id = request.POST["to_silo_id"]
	getSourceFrom = DataField.objects.all().filter(silo__id=from_silo_id).distinct("name")
	getSourceTo = DataField.objects.all().filter(silo__id=to_silo_id).distinct("name")
	
	return render_to_response("display/merge-column-form.html", {'getSourceFrom':getSourceFrom,'getSourceTo':getSourceTo,'from_silo_id':from_silo_id,'to_silo_id':to_silo_id})


