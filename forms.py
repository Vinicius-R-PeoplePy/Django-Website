from django import forms
from django.contrib.auth.hashers import make_password
from .models import User 

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User 
        fields = ['name', 'username', 'email', 'birthdate', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user