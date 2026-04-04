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