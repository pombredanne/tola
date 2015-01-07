from django.forms import ModelForm
from silo.models import Silo
import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Reset, HTML, Button, Row, Field
from crispy_forms.bootstrap import  FormActions

class SiloForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SiloForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # Append the read_id for edits and save button
        self.helper.layout.append(Submit('save', 'save'))
    class Meta:
        model = Silo
        fields = ['id', 'name', 'description', 'source','owner']