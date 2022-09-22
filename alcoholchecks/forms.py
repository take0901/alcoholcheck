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
        fields = ['alcohol', 'carnumber']
        labels = {'alcohol':"アルコール検知の有無", 'carnumber':"車両ナンバー"}