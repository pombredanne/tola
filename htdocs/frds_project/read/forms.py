from django.forms import ModelForm
from read.models import Read

class ReadForm(ModelForm):
	class Meta:
		model = Read
		fields = ['read_name', 'read_url', 'description','type','owner']