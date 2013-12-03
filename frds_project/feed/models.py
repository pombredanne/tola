from django.db import models
from django.contrib import admin
#from silo.models import Silo


# Create your models here.

class FeedType(models.Model):
	description = models.CharField(max_length=765, blank=True)
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True)

class FeedTypeAdmin(admin.ModelAdmin):
	list_display = ('feed_type','description','create_date','edit_date')
	display = 'Feed Type'
	
class Feed(models.Model):
	owner = models.ForeignKey('auth.User')
	feed_type = models.ForeignKey(FeedType)
	name = models.TextField()
	description = models.TextField()
	create_date = models.DateTimeField(null=True, blank=True)
	published = models.BooleanField()
	class Meta:
		ordering = ('create_date',)

	def save(self, *args, **kwargs):
		super(Feed, self).save(*args, **kwargs)

class FeedAdmin(admin.ModelAdmin):
	list_display = ('owner','feed_type_id','feed_name','feed_url','description','create_date')
	display = 'Data Feeds'