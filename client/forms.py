from django import forms
from .models import Client
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean_confirm(self):
        if self.cleaned_data['confirm'] != self.cleaned_data['password']:
            raise ValidationError("Parollar bir xil bo'lishi shart.")

        return self.cleaned_data['confirm']

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'username', 'password', 'confirm', 'email')
        widgets = {
            'password': forms.PasswordInput
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
