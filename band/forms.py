from django import forms
from .models import Concert


class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = '__all__'

