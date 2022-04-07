from django import forms
# from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, help_text='email halnus' )
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)