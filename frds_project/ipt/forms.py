from django.forms import ModelForm
from ipt.models import Program, Indicator

class ProgramForm(ModelForm):
	class Meta:
		model = Program
		fields = ['grantid','name','sector', 'storagebin_url', 'description','sector','owner']


class IndicatorForm(ModelForm):
	class Meta:
		model = Indicator
		fields = ['type','name', 'description', 'activity','period','sector','owner','program']