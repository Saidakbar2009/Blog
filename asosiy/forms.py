from django import forms
from .models import Maqola

class MaqolaForm(forms.ModelForm):
    class Meta:
        model = Maqola
        fields = ['sarlavha', 'sana', 'mavzu', 'matn', 'muallif']
