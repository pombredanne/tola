from django.db import models
from django.contrib import admin
#from silo.models import Silo


# Create your models here.
class Read(models.Model):
	owner = models.ForeignKey('auth.User')
	read_name = models.TextField()
	read_url = models.CharField(max_length=100, blank=True, default='')
	description = models.TextField()
	create_date = models.DateTimeField(null=True, blank=True)
	class Meta:
		ordering = ('create_date',)

	def save(self, *args, **kwargs):
		super(Read, self).save(*args, **kwargs)

class ReadAdmin(admin.ModelAdmin):
	list_display = ('owner','read_name','read_url','description','create_date')
	display = 'Read Data Feeds'
	
class ReadType(models.Model):
	read_type = models.CharField(max_length=135, blank=True)
	description = models.CharField(max_length=765, blank=True)
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True)
	Read = models.ManyToManyField(Read)

class ReadTypeAdmin(admin.ModelAdmin):
	list_display = ('read_type','description','create_date','edit_date')
	display = 'Read Type'