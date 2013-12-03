from django.db import models
from django.contrib import admin
from read.models import Read
from feed.models import Feed


# Create your models here.
class Silo(models.Model):
	owner = models.ForeignKey('auth.User')
	name = models.TextField()
	source = models.ForeignKey(Read)
	description = models.TextField()
	create_date = models.DateTimeField(null=True, blank=True)
	class Meta:
		ordering = ('create_date',)

	def save(self, *args, **kwargs):
		super(Silo, self).save(*args, **kwargs)

class SiloAdmin(admin.ModelAdmin):
	list_display = ('owner','name','source','description','create_date')
	display = 'Data Feeds'
	
class DataField(models.Model):
	silo = models.ForeignKey(Silo)
	name = models.CharField(max_length=765, blank=True)
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True)

class DataFieldAdmin(admin.ModelAdmin):
	list_display = ('silo','name','create_date','edit_date')
	display = 'Data Fields'

class ValueType(models.Model):
	value_type = models.CharField(max_length=255)
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True)

class ValueTypeAdmin(admin.ModelAdmin):
	list_display = ('value_type','create_date','edit_date')
	display = 'Types of Data Values'

class ValueStore(models.Model):
	value_type = models.ForeignKey(ValueType)
	field = models.ForeignKey(DataField)
	int_store = models.BigIntegerField(null=True, blank=True)
	char_store = models.CharField(null=True, blank=True,max_length=1000)
	text_store = models.TextField(null=True, blank=True)
	date_store = models.DateTimeField(null=True, blank=True)
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True)

class ValueStoreAdmin(admin.ModelAdmin):
	list_display = ('column','value_type','field','int_store','char_store','text_store','date_store','create_date','edit_date')
	display = 'Stored Values'

