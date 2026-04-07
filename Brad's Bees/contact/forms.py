from django import forms
from django.forms import ModelForm
from contact.models import *

class SubmissionForm(forms.ModelForm):
    images = forms.ImageField(required=False)

    class Meta:
        model = Submission
        fields = [
            'name',
            'email',
            'phone',
            'service',
            'message',
        ]
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email'
    }))
    phone = forms.CharField(max_length=12, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'XXX-XXX-XXXX'
    }))
    service = forms.CharField(max_length=20, required=True)
    message = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Tell us about your needs...'
    }))