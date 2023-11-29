# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)