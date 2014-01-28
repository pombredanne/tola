from django.forms import ModelForm
from silo.models import ValueStore

class EditForm(ModelForm):
	class Meta:
		model = ValueStore
		fields = [ 'field','char_store','create_date','edit_date']
