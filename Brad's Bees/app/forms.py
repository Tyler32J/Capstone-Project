from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from .models import Submission

letters_only = RegexValidator(
    regex=r'^[A-Za-z\s]+$',
    message=f'This field must contain letters and spaces only.'
)

phone_validator = RegexValidator(
    regex=r'^\d{3}-\d{3}-\d{4}$',
    message='Phone number must be in the format XXX-XXX-XXXX.'
)


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput(attrs={
            'class': 'form-input'
        }))
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        if isinstance(data, (list, tuple)):
            return [super().clean(d, initial) for d in data]
        return super().clean(data, initial)



class SubmissionForm(forms.ModelForm):
    images = MultipleFileField(required=False)

    class Meta:
        model = Submission
        fields = [
            'name',
            'email',
            'phone',
            'service',
            'message',
        ]

    name = forms.CharField(
        max_length=50,
        required=True,
        validators=[letters_only],
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your name'
        })
    )

    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your Email'
        })
    )

    phone = forms.CharField(
        max_length=12,
        required=True,
        validators=[phone_validator],
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'XXX-XXX-XXXX'
        })
    )

    service = forms.ChoiceField(
        choices=Submission.SERVICE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    message = forms.CharField(
        max_length=999999,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'placeholder': 'Tell us about your needs...',
            'rows': 4
        })
    )