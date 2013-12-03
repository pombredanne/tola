from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
from django.shortcuts import render_to_response
from datetime import date
import os
import urllib2
import json 
import unicodedata
from django.http import HttpResponseRedirect
from django.db import models
from silo.models import Silo, DataField, ValueStore, ValueType
from read.models import Read
from read.forms import ReadForm

def initRead(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ReadForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            new_read = form.save()
            return HttpResponseRedirect('/json/') # Redirect after POST
    else:
        form = ReadForm() # An unbound form

    return render(request, 'read.html', {
        'form': form,
    })

def getJSON(request):
	read_obj = Read.objects.latest('id')
	#get JSON based data from URL
	json_file = urllib2.urlopen(read_obj.read_url)
	#create object from JSON String
	data = json.load(json_file)
	json_file.close()
	
	for row in data:
		vars_to_display = []
		keys_to_display = []
		for new_key,new_value in row.iteritems():
			if new_value is not "" and new_value is not None:
				today = date.today()
				today.strftime('%Y-%m-%d')
				today = str(today)
				print new_key
				print new_value
				vars_to_display.append(new_value)
				keys_to_display.append(new_key)
					
	from django.shortcuts import render 
	return render_to_response("read-json.html", {'keys_to_display':keys_to_display,'vars_to_display':vars_to_display})

def saveJSON(request):
	current_silo = Silo.objects.get(pk=1)
	#get JSON based data from URL
	json_file = urllib2.urlopen('https://www.formhub.org/api/v1/data/glind/30287')
	#create object from JSON String
	data = json.load(json_file)
	json_file.close()
	
	for row in data:
		vars_to_sql = []
		keys_to_sql = []
		for new_key,new_value in row.iteritems():
			if new_value is not "" and new_value is not None:
				today = date.today()
				today.strftime('%Y-%m-%d')
				today = str(today)
				print new_key
				print new_value
				new_field = DataField(silo=current_silo, name=new_key, create_date=today,edit_date=today)
				new_field.save()
				
				check_type=type(new_value)
				
				print check_type
				
				if check_type == models.CharField:
					#CharField specific code
					check_type="Char"
					type_value = ValueType.objects.get(value_type=check_type)
					new_value = ValueStore(value_type=type_value, char_store=new_value, create_date=today,edit_date=today)
				elif check_type == models.IntegerField:
					check_type="Int"
					type_value = ValueType.objects.get(value_type=check_type)
					new_value = ValueStore(value_type=type_value, int_store=new_value, create_date=today,edit_date=today)
				elif check_type == models.DateField:
					check_type="Date"
					type_value = ValueType.objects.get(value_type=check_type)
					new_value = ValueStore(value_type=type_value, date_store=new_value, create_date=today,edit_date=today)
				else: 
					check_type="Char"
					type_value = ValueType.objects.get(value_type=check_type)
					new_value = ValueStore(value_type=type_value, char_store=new_value, create_date=today,edit_date=today)
					
				
				new_value.save()
	
	from django.shortcuts import render 
	return render(request, "read-json.html", data)
 
