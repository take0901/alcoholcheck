from django import forms
from .models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['alcohol', 'carnumber']
        labels = {'alcohol':"アルコール検知の結果", 'carnumber':"車両ナンバー"}