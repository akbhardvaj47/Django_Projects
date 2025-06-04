from django import forms

class UserForm(forms.Form):
    num1 = forms.CharField(max_length=100) 
    num2 = forms.CharField(max_length=100)
    num3 = forms.EmailField()  




