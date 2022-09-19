from django import forms
from .models import Month, Info

class MonthForm(forms.ModelForm):
    class Meta:
        model = Month
        fields = ['month']
        labels = {'month':""}

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['alcohol']
        labels = {'alcohol':""}