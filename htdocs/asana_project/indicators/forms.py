from django.forms import ModelForm
from indicators.models import Program, Indicator

class ProgramForm(ModelForm):
	class Meta:
		model = Program
		fields = ['grantid','name','sector', 'storagebin_url', 'description','sector','owner']


class IndicatorForm(ModelForm):
	class Meta:
		model = Indicator
		fields = ['indicator_type','name', 'description', 'activity','period','sector','target','target_actual','dissaggregation_type','budget','budget_actual','owner','program']

class ProgramIndicatorForm(ModelForm):
	class Meta:
		model = Indicator
		fields = ['indicator_type','name', 'description', 'activity','period','sector','target','target_actual','dissaggregation_type','budget','budget_actual','owner','program']