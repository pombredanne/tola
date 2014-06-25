from django.forms import ModelForm
from silo.models import ValueStore,DataField


class EditForm(ModelForm):
    class Meta:
        model = ValueStore
        fields = ['field','char_store','create_date','edit_date']


class FieldEditForm(ModelForm):
    class Meta:
        model = DataField
        fields = ['original_name','name','is_uid','create_date','edit_date']