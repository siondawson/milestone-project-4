from django import forms
from .models import Concert
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _


class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = [
            'date',
            'venue',
            'city',
            'tickets'
        ]

    def __init__(self, *args, **kwargs):
        super(ConcertForm, self).__init__(*args, **kwargs)
        placeholders = {
            'date': 'dd-mm-yyyy',
            'venue': 'venue',
            'city': 'city',
            'tickets': 'tickets',
        }

        for field in self.fields:
            self.fields['date'].widget = TextInput(attrs={
                'placeholder': placeholders['date'],
                'class': 'border-black rounded-0 mb-3 profile-form-input',
                'autocomplete': 'off',  # Disable autocomplete for date field
            })
            self.fields['date'].input_formats = ['%d-%m-%Y %H:%M']  # Set the desired input format
            self.fields['date'].label = _('Date (dd-mm-yyyy hh:mm)')  # Optional: Set a custom label
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black \
                                            rounded-0 mb-3 profile-form-input'


        
        
