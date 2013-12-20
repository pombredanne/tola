from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
from datetime import date
import os
import urllib2
import json 
import unicodedata
from django.http import HttpResponseRedirect
from django.db import models
from silo.models import Silo, DataField, ValueStore, ValueType, Read
from read.models import Read
from silo.forms import SiloForm
from django.shortcuts import render_to_response


# Create your views here.
def doMerge(request):
		
	from_silo_id = request.POST["from_silo_id"]
	to_silo_id = request.POST["to_silo_id"]
	getSourceFrom = DataField.objects.all().filter(silo__id=from_silo_id).distinct("name")
	#update each column, set value to evaluated column name which will equal the selcted value in from column drop down
	for column in getSourceFrom:
		update= ValueStore.objects.filter(field__name=column.name).update(field=request.POST.get(column.name))
	#delete silo and original fields
	deleteSilo = Silo.objects.filter(id=from_silo_id).delete
	#get new combined silo values then display them
	getSilo = ValueStore.objects.all().filter(field__silo__id=to_silo_id)

	return render(request,"display/stored_values.html", {'getSilo':getSilo}) 

#EDIT-SILO
def editSilo(request,id):
	
	if request.method == 'POST': # If the form has been submitted...
		form = SiloForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# save data to read
			new_read = form.save()
			return HttpResponseRedirect('silo') # Redirect after POST to getLogin
	else:
		getSilo=Silo.objects.get(pk=id)
		form = SiloForm(instance=getSilo) # An unbound form

	return render(request, 'silo/edit.html', {
		'form': form,
	})
