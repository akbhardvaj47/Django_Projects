from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ( 'first_name','last_name','email','username', 'password1', 'password2')
    

    