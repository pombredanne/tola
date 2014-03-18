from django.db import models
from django.contrib import admin
#from silo.models import Silo

# Create your models here.
class IndicatorType(models.Model):
	type = models.CharField(max_length=135, blank=True)
	description = models.CharField(max_length=765, blank=True)
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True)
	
	def __unicode__(self):
		return self.type

class IndicatorTypeAdmin(admin.ModelAdmin):
	list_display = ('type','description','create_date','edit_date')
	display = 'Indicator Type'

class Sector(models.Model):
	sector = models.CharField(max_length=135, blank=True)
	description = models.CharField(max_length=765, blank=True)
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True)
	
	def __unicode__(self):
		return self.sector

class SectorAdmin(admin.ModelAdmin):
	list_display = ('sector','description','create_date','edit_date')
	display = 'Sector'

class TVAPeriod(models.Model):
	periodType = models.ForeignKey(IndicatorType)
	target = models.CharField(max_length=765, blank=True)
	actual = models.CharField(max_length=765, blank=True)
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True)
	
	def __unicode__(self):
		return self.periodType

class TVAPeriodAdmin(admin.ModelAdmin):
	list_display = ('periodType','target','actual','create_date','edit_date')
	display = 'Target vs Actuals'

class ActivityData(models.Model):
	url = models.CharField(max_length=765, blank=True)
	description = models.CharField(max_length=765, blank=True)
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True)
	
	def __unicode__(self):
		return self.url
		
class ActivityDataAdmin(admin.ModelAdmin):
	list_display = ('url','description','create_date','edit_date')
	display = 'Activity Data'

class PeriodType(models.Model):
	type = models.CharField(max_length=135, blank=True)
	description = models.CharField(max_length=765, blank=True)
	length = models.CharField(max_length=135, blank=True)
	
	def __unicode__(self):
		return self.type

class PeriodTypeAdmin(admin.ModelAdmin):
	list_display = ('type','description','length')
	display = 'Period Types'

class Program(models.Model):
	owner = models.ForeignKey('auth.User')
	grantid = models.CharField(max_length=135, blank=True)
	name = models.CharField(max_length=765, blank=True)
	sector = models.ForeignKey(Sector)
	description = models.CharField(max_length=765, blank=True)
	storagebin_url = models.CharField(max_length=765, blank=True)
	create_date = models.DateTimeField(null=True, blank=True)
	edit_date = models.DateTimeField(null=True, blank=True)
	
	def __unicode__(self):
		return self.name

class ProgramAdmin(admin.ModelAdmin):
	list_display = ('grantid','name','sector','description','storagebin_url','create_date','edit_date')
	display = 'Programs'

class Indicator(models.Model):
	owner = models.ForeignKey('auth.User')
	type = models.ForeignKey(IndicatorType)
	program = models.ForeignKey(Program)
	name = models.TextField()
	activity = models.ForeignKey(ActivityData)
	sector = models.ForeignKey(Sector)
	description = models.TextField()
	create_date = models.DateTimeField(null=True, blank=True)
	target = models.CharField(max_length=135, blank=True)
	target_actual = models.CharField(max_length=135, blank=True)
	budget = models.CharField(max_length=135, blank=True)
	budget_actual = models.CharField(max_length=135, blank=True)
	period = models.ForeignKey(PeriodType)
	class Meta:
		ordering = ('create_date',)

	def save(self, *args, **kwargs):
		super(Indicator, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.name

class IndicatorAdmin(admin.ModelAdmin):
	list_display = ('owner','type','name','sector','activityData','description')
	display = 'Indicators'
