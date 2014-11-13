from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from crispy_forms.layout import Layout, Submit, Reset
import floppyforms as forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback


    severity = forms.ChoiceField(
        label="Priority",
        choices=(("High", "High"), ("Medium", "Medium"), ("Low", "Low")),
        widget=forms.Select,
        initial='2',
        required=True,
    )

    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-6'
    helper.form_error_title = 'Form Errors'
    helper.error_text_inline = True
    helper.help_text_inline = True
    helper.html5_required = True
    helper.layout = Layout(Fieldset('', 'submitter', 'note', 'page', 'severity'),Submit('submit', 'Submit', css_class='btn-default'), Reset('reset', 'Reset', css_class='btn-warning'))

