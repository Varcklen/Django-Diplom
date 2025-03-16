from django import forms
from .models import UserMessage

class UserMessageForm(forms.ModelForm):

    class Meta:
        model = UserMessage
        fields = ('name', 'email', 'phone', 'message',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': "name",
                'type': 'text',
                'placeholder': "Your Name",
                'data-sb-validations': "required",
                }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'id': "email",
                'type': 'email',
                'placeholder': "Your Email",
                'data-sb-validations': "required,email",
                }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': "phone",
                'type': 'tel',
                'placeholder': "Your Phone",
                'data-sb-validations': "required",
                }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': "message",
                'placeholder': "Your Message",
                'data-sb-validations': "required",
                }),
        }