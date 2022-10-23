from django import forms
from .models import Information

class InfoForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['year', 'month', 'motouke', 'kouzi', 'place', 'color_number', 'other']
        labels = {'year':"年", 'month':"月", 'motouke':"元請", 'kouzi':"工事名",
                    'place':"場所", 'color_number':'色番号', 'other':"備考"}
