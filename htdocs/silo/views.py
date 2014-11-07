from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
import datetime
import os
import urllib2
import json
import unicodedata
from django.http import HttpResponseRedirect
from django.db import models
from silo.models import Silo, DataField, ValueStore, Read
from read.models import Read
from silo.forms import SiloForm
from django.shortcuts import render_to_response
from django.shortcuts import render


# Merge 2 silos together.
def doMerge(request):
    from_silo_id = request.POST["from_silo_id"]
    to_silo_id = request.POST["to_silo_id"]
    getSourceFrom = DataField.objects.all().filter(silo__id=from_silo_id)
    # update each column, set value to evaluated column name which will equal the selected value in from column drop down
    for column in getSourceFrom:
        #print request.POST.get(column.name)
        print "column name = "
        print column.name
        print " column name value = "
        print request.POST.get(column.name)
        #If it's a new column just update the column to use the new silo
        if request.POST.get(column.name) == "0":
            update_column_silo = DataField.objects.filter(name=column.name).update(silo=to_silo_id)
        #if it's an existing column update the values to use the existing column
        elif request.POST.get(column.name) != "Ignore" and request.POST.get(column.name) != "0":
            update_column_name = DataField.objects.filter(name=column.name).update(name=request.POST.get(column.name), silo=to_silo_id)

    #delete silo and original fields
    deleteSilo = Silo.objects.get(pk=from_silo_id).delete()
    #get new combined silo values then display them
    getSilo = ValueStore.objects.all().filter(field__silo__id=to_silo_id)

    return render(request, "display/stored_values.html", {'getSilo': getSilo})


# Edit existing silo meta data
def editSilo(request, id):
    getSilo = Silo.objects.get(pk=id)

    if request.method == 'POST':  # If the form has been submitted...
        form = SiloForm(request.POST, instance=getSilo)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # save data to read
            updated = form.save()
            return HttpResponseRedirect('/display')  # Redirect after POST to getLogin
        else:
            print form.errors
            return HttpResponse("Form Did Not Save!")
    else:

        form = SiloForm(instance=getSilo)  # An unbound form

    return render(request, 'silo/edit.html', {
        'form': form, 'silo_id': id,
    })


#DELETE-SILO
def deleteSilo(request, id):
    deleteSilo = Silo.objects.get(pk=id).delete()

    return render(request, 'silo/delete.html')
