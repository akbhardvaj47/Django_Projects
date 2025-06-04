from django import forms

class MyForm(forms.Form):
    num1=forms.CharField(label='Enter Number 1',)
    num2=forms.CharField(label='Enter Number 2')
