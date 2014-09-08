from django.forms import ModelForm
from read.models import Read
from .models import Token
from django.forms.models import inlineformset_factory


class ReadForm(ModelForm):
    class Meta:
        model = Read


TokenFormSet = inlineformset_factory(Read, Token, fields=('read_token', 'read_secret'), can_delete=False, extra=1)
