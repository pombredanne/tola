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
from models import Program
from ipt.forms import ProgramForm, IndicatorForm
from django.shortcuts import render_to_response

def home(request):	
	#get all of the Programs
	getPrograms = Program.objects.all()

	return render(request, 'ipt/home.html',{'getPrograms':getPrograms})

def dashboard(request):

	return render(request, 'ipt/dashboard.html')

def indicator(request):
	if request.method == 'POST': # If the form has been submitted...
		form = IndicatorForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# save data to read
			new = form.save()
			return HttpResponseRedirect('/ipt/indicator') # Redirect after POST to getLogin
	else:
		form = IndicatorForm() # An unbound form
	
	return render(request, 'ipt/indicator.html', {'form': form,})

def program(request):
	if request.method == 'POST': # If the form has been submitted...
		form = ProgramForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# save data to read
			new = form.save()
			return HttpResponseRedirect('/ipt/indicator') # Redirect after POST to getLogin
	else:
		form = ProgramForm() # An unbound form

	return render(request, 'ipt/program.html', {'form': form,})
 
def tool(request):

	return render(request, 'ipt/tool.html')
