from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

class SignupForm(UserCreationForm):
    e
    class Meta:
        model = User
        fields = ['username','password1','password2']