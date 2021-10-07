from django import forms
from django.contrib.auth import get_user_model

class FastSignupForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data['email']

        users = get_user_model().objects.filter(email=email)
        if len(users) > 0:
            raise forms.ValidationError("Email is existed")

        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        
        if len(password) < 8:
            raise forms.ValidationError("Password is to short")

        return password