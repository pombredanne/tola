from django.db import models
from django.contrib import admin
from silo.models import Silo,DataField,ValueStore
	
class Feed(models.Model):
	owner = models.ForeignKey('auth.User')
	source = models.ForeignKey(Silo)
	create_date = models.DateTimeField(null=True, blank=True)
	published = models.BooleanField()
	class Meta:
		ordering = ('create_date',)

	def save(self, *args, **kwargs):
		super(Feed, self).save(*args, **kwargs)

class FeedAdmin(admin.ModelAdmin):
	list_display = ('owner','feed_type_id','feed_name','feed_url','description','create_date')
	display = 'Data Feeds'