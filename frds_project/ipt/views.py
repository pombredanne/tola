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
	"""
	Create an Indicator
	"""
	if request.method == 'POST': # If the form has been submitted...
		form = IndicatorForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# save data to read
			new = form.save()
			return HttpResponseRedirect('/ipt/indicator') # Redirect after POST to getLogin
	else:
		form = IndicatorForm() # An unbound form
	
	return render(request, 'ipt/indicator.html', {'form': form,})

def editIndicator(request,id):
	"""
	Edit an Indicator
	"""
	if request.method == 'POST': # If the form has been submitted...
		form = IndicatorForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# save data to read
			update = Indicator.objects.get(pk=id)
			form = IndicatorForm(request.POST, instance=update)
			new = form.save(commit=True)
			return HttpResponseRedirect('ipt/editIndicator/' + id)
		else:
			print "not valid"
	else:
		value= get_object_or_404(Indicator, pk=id)
		form = IndicatorForm(instance=value) # An unbound form
	
	return render(request, 'ipt/indicator.html', {'form': form,'value':value})
 

def program(request):
	"""
	Create a program
	"""
	if request.method == 'POST': # If the form has been submitted...
		form = ProgramForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# save data to read
			new = form.save()
			return HttpResponseRedirect('/ipt/indicator') # Redirect after POST to getLogin
	else:
		form = ProgramForm() # An unbound form

	return render(request, 'ipt/program.html', {'form': form,})

def editProgram(request,id):
	"""
	Edit a program
	"""
	if request.method == 'POST': # If the form has been submitted...
		form = ProgramForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# save data to read
			update = Program.objects.get(pk=id)
			form = ProgramForm(request.POST, instance=update)
			new = form.save(commit=True)
			return HttpResponseRedirect('ipt/editProgram/' + id)
		else:
			print "not valid"
	else:
		value= get_object_or_404(Program, pk=id)
		form = ProgramForm(instance=value) # An unbound form
	
	return render(request, 'ipt/program.html', {'form': form,'value':value})

def programIndicator(request,id):
	
	getProgramIndicators = Program.objects.get(id=id)
	
	return render(request, 'ipt/programIndicator.html', {'program':getProgramIndicators})
 
def tool(request):

	return render(request, 'ipt/tool.html')
