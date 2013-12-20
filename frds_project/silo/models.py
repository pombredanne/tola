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
	
	def __unicode__(self):
		return self.name

class SiloAdmin(admin.ModelAdmin):
	list_display = ('owner','name','source','description','create_date')
	display = 'Data Feeds'
	
class DataField(models.Model):
	silo = models.ForeignKey(Silo)
	name = models.CharField(max_length=765, blank=True)
	is_uid = models.BooleanField()
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
		return self.name

class DataFieldAdmin(admin.ModelAdmin):
	list_display = ('silo','name','is_uid','create_date','edit_date')
	display = 'Data Fields'

class ValueType(models.Model):
	value_type = models.CharField(max_length=255)
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True)
	
	def __unicode__(self):
		return self.value_type

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
	date_time_store = models.DateField(null=True, blank=True)
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True) 
	
	#set the label based on the type of value store
	def __unicode__(self):
		if self.value_type.value_type is "char":
			self.value_type.value_type + ": " + self.char_store
		elif self.value_type.value_type is "int":
			self.value_type.value_type + ": " + self.int_store
		elif self.value_type.value_type is "date":
			self.value_type.value_type + ": " + self.date_store
		elif self.value_type.value_type is "date_time":
			self.value_type.value_type + ": " + self.date_time_store
		else:
			self.value_type.value_type + ": " + self.char_store
		return self.value_type.value_type + ": " + self.char_store

class ValueStoreAdmin(admin.ModelAdmin):
	list_display = ('value_type','field','int_store','char_store','text_store','date_store','date_time_store','create_date','edit_date')
	display = 'Stored Values'


