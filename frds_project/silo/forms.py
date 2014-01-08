from django.forms import ModelForm
from silo.models import Silo

class SiloForm(ModelForm):
	class Meta:
		model = Silo
		fields = ['id', 'name', 'description', 'source','owner']