from django import forms
from .models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['alcohol', 'carnumber', 'varified_by', 'how_to']
        labels = {'alcohol':"アルコール検知の結果", 'carnumber':"車両ナンバー",
                   'varified_by': "確認者", 'how_to': '確認方法'}
        