import datetime
import urllib2
import json
import base64

from django.http import HttpResponseRedirect
from silo.models import Silo, DataField, ValueStore
from read.models import Read
from read.forms import ReadForm
from django.shortcuts import render_to_response
from django.shortcuts import render

"""
List of Current Read sources that can be updated or edited
"""
def home(request):
    getReads = Read.objects.all()

    return render(request, 'read/home.html', {'getReads': getReads, })


"""
Create a form to get feed info then save data to Read 
and re-direct to getJSON funtion
"""
def initRead(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = ReadForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # save data to read
            new_read = form.save()
            return HttpResponseRedirect('/login')  # Redirect after POST to getLogin
    else:
        form = ReadForm()  # An unbound form

    return render(request, 'read/read.html', {
        'form': form,
    })

"""
Show a read data source and allow user to edit it
"""
def showRead(request, id):
    getRead = Read.objects.get(pk=id)

    if request.method == 'POST':  # If the form has been submitted...
        form = ReadForm(request.POST, instance=getRead)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # save data to read
            new_read = form.save()
            return HttpResponseRedirect('/login')  # Redirect after POST to getLogin
    else:
        form = ReadForm(instance=getRead)  # An unbound form

    return render(request, 'read/read.html', {
        'form': form,
    })

"""
Some services require a login provide user with a
login to service if needed and select a silo
"""
def getLogin(request):
    # get all of the silo info to pass to the form
    get_silo = Silo.objects.all()

    # display login form
    return render(request, 'read/login.html', {'get_silo': get_silo})


"""
Get JSON feed info from form then grab data
"""
def getJSON(request):
    # retrieve submitted Feed info from database
    read_obj = Read.objects.latest('id')
    # set date time stamp
    today = datetime.date.today()
    today.strftime('%Y-%m-%d')
    today = str(today)
    #New silo or existing
    if request.POST['new_silo']:
        print "NEW"
        new_silo = Silo(name=request.POST['new_silo'], source=read_obj, owner=read_obj.owner, create_date=today)
        new_silo.save()
        silo_id = new_silo.id
    else:
        print "EXISTING"
        silo_id = request.POST['silo_id']

    #get auth info from form post then encode and add to the request header
    username = request.POST['user_name']
    password = request.POST['password']
    base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
    request = urllib2.Request(read_obj.read_url)
    request.add_header("Authorization", "Basic %s" % base64string)
    #retrieve JSON data from formhub via auth info
    json_file = urllib2.urlopen(request)

    #create object from JSON String
    data = json.load(json_file)
    json_file.close()
    #loop over data and insert create and edit dates and append to dict
    for row in data:
        for new_label, new_value in row.iteritems():
            if new_value is not "" and new_label is not None:
                #save to DB
                saveJSON(new_value, new_label, silo_id)

    #get fields to display back to user for verification
    getFields = DataField.objects.filter(silo_id=silo_id)

    #send the keys and vars from the json data to the template along with submitted feed info and silos for new form
    return render_to_response("read/show-columns.html", {'getFields': getFields, 'silo_id': silo_id})


"""
Set the PK for each row by allowing the user to select a column
"""
def updateUID(request):
    for row in request.POST['is_uid']:
        update_uid = DataField.objects.update(is_uid=1)

    get_silo = ValueStore.objects.all().filter(field__silo_id=request.POST['silo_id'])

    return render(request, "read/show-data.html", {'get_silo': get_silo})


"""
Function call no template associated with this
Save JSON file data into data store and silo
"""
def saveJSON(new_value, new_label, silo_id):
    # Need a silo set object to gather silos into programs
    current_silo = Silo.objects.get(pk=silo_id)
    # set date time stamp
    today = datetime.date.today()
    today.strftime('%Y-%m-%d')
    today = str(today)
    if new_value is not "" and new_value is not None:
        new_field = DataField(silo=current_silo, name=new_label, create_date=today, edit_date=today)
        new_field.save()
        #get the field id
        latest = DataField.objects.latest('id')

        new_value = ValueStore(field_id=latest.id, char_store=new_value, create_date=today, edit_date=today)

        new_value.save()
 
