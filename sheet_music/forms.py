from django import forms
from .models import Sheetmusic, Category


class SheetmusicForm(forms.ModelForm):

    class Meta:
        model = Sheetmusic
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
