from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = "__all__"


class MarksheetForm(forms.ModelForm):
    class Meta:
        model = Marksheet
        fields = "__all__"
