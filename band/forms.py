from django import forms
from .models import Concert


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
            self.fields['Tickets'].label = "Ticket or external info link"

