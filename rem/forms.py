from django import forms
from datetime import datetime
class RemForm(forms.Form):
    text = forms.CharField(max_length=40)
    time = forms.DateField()
