from django.forms import ModelForm
from .models import Marksheet


class MarksheetForm(ModelForm):
    class Meta:
        model = Marksheet
        fields = "__all__"