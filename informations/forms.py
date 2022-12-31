from django import forms
from .models import Information

class InfoForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['color_number', 'other']
        labels = {'color_number':'色番号', 'other':"備考"}
