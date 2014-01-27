from django.forms import ModelForm
from silo.models import ValueStore

class EditForm(ModelForm):
	class Meta:
		model = ValueStore
		fields = ['value_type', 'field', 'int_store','char_store','text_store','date_store','date_time_store','create_date','edit_date']