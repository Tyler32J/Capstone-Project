from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from contact.models import *

letters_only = RegexValidator(
    regex=r'^[A-Za-z\s]+$',
    message=f'This field must contain letters and spaces only.'
)

phone_validator = RegexValidator(
    regex=r'^\d{3}-\d{3}-\d{4}$',
    message='Phone number must be in the format XXX-XXX-XXXX.'
)

class SubmissionForm(forms.ModelForm):
    images = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = Submission
        fields = [
            'name',
            'email',
            'phone',
            'service',
            'message',
        ]
    name = forms.CharField(max_length=50, required=True, validators=[letters_only], widget=forms.TextInput(attrs={
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email'
    }))
    phone = forms.CharField(max_length=12, required=True, validators=[phone_validator], widget=forms.TextInput(attrs={
        'placeholder': 'XXX-XXX-XXXX'
    }))
    service = forms.ChoiceField(choices=Submission.SERVICE_CHOICES)#(max_length=20, required=True)
    message = forms.CharField(max_length=999999, required=True, widget=forms.Textarea(attrs={
        'placeholder': 'Tell us about your needs...'
    }))