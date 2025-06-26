from django import forms
from projectapp.models import carlist

class carform(forms.ModelForm):
    class Meta:
        model=carlist
        fields ='__all__'